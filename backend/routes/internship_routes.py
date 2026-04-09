import os
import json
import urllib.request
import urllib.error
from flask import Blueprint, request, jsonify

internship_bp = Blueprint('internship', __name__)

FALLBACK_INTERNSHIPS = [
    {
        "company": "Zerodha",
        "role": "Finance Intern",
        "location": "Remote",
        "stipend": "₹8,000",
        "duration": "2 months",
        "skills": ["Finance", "Excel"],
        "apply_link": "https://zerodha.com/careers",
        "deadline": "Rolling"
    },
    {
        "company": "Razorpay",
        "role": "Fintech Intern",
        "location": "Bangalore",
        "stipend": "₹12,000",
        "duration": "3 months",
        "skills": ["Data Analysis", "Python"],
        "apply_link": "https://razorpay.com/jobs/",
        "deadline": "Rolling"
    },
    {
        "company": "HDFC Bank",
        "role": "Banking Intern",
        "location": "Mumbai",
        "stipend": "₹6,000",
        "duration": "2 months",
        "skills": ["Accounting", "Communication"],
        "apply_link": "https://www.hdfcbank.com/personal/about-us/careers",
        "deadline": "Rolling"
    },
    {
        "company": "Groww",
        "role": "Investment Research Intern",
        "location": "Remote",
        "stipend": "₹10,000",
        "duration": "3 months",
        "skills": ["Market Research", "Finance"],
        "apply_link": "https://groww.in/careers",
        "deadline": "Rolling"
    }
]

FALLBACK_COMPANIES = [
    {"name": "Zerodha", "industry": "Finance", "reason": "Great for learning stock markets", "link": "https://zerodha.com/careers"},
    {"name": "Razorpay", "industry": "Fintech", "reason": "Best in class payment industry exposure", "link": "https://razorpay.com/jobs/"},
    {"name": "Cred", "industry": "Fintech", "reason": "Fast paced environment to grow", "link": "https://careers.cred.club/"},
    {"name": "TCS", "industry": "Technology", "reason": "Industry standard training for youth", "link": "https://www.tcs.com/careers"},
    {"name": "HDFC Bank", "industry": "Banking", "reason": "Largest private sector bank in India", "link": "https://www.hdfcbank.com/personal/about-us/careers"},
    {"name": "Groww", "industry": "Investment", "reason": "Learn wealth management", "link": "https://groww.in/careers"},
]


import time
from datetime import datetime

# Simple in-memory cache to mirror Node.js instructions
cache = {}

@internship_bp.route('/live', methods=['POST'])
def get_live_internships():
    try:
        data = request.get_json()
        interests = data.get('interests', [])
        completedModules = data.get('completedModules', [])
        ageGroup = data.get('ageGroup', "13-19")
        
        # Build cache key
        inter_str = ",".join(sorted(interests))
        mod_str = ",".join(sorted([str(m) for m in completedModules]))
        cache_key = f"{inter_str}_{mod_str}"

        # Check cache (valid for 30 mins)
        if cache_key in cache:
            if (time.time() - cache[cache_key]['time']) < (30 * 60):
                return jsonify(cache[cache_key]['data']), 200

        # Build prompt strings
        interests_desc = ", ".join(interests) if interests else "General Finance and Tech"
        modules_desc = ", ".join([str(m) for m in completedModules]) if completedModules else "none yet"

        from google import genai
        
        # Load API key securely from environment — never hardcode keys
        gemini_api_key = os.environ.get('GEMINI_API_KEY')
        if not gemini_api_key:
            return jsonify({"error": "Server configuration error: GEMINI_API_KEY is not set."}), 503

        client = genai.Client(api_key=gemini_api_key)

        prompt = f"""You are an internship research assistant for teenagers aged {ageGroup}.
Given interests: {interests_desc}.
Completed learning modules: {modules_desc}.

Return a JSON object with two keys:
1. "internships": array of 8-12 real internship opportunities from major companies and startups relevant to the interests above. Each object must have:
   - role (string): job title
   - company (string): company name
   - location (string): e.g. "Remote", "Bengaluru", "Mumbai", "Delhi", "Hyderabad", "Pan India"
   - stipend (string): e.g. "₹10,000/month", "₹5,000/month", "Unpaid", "Performance-based"
   - duration (string): e.g. "2 months", "3 months", "6 weeks"
   - deadline (string): a realistic future ISO date string (within next 60-90 days from today) or null for rolling
   - apply_link (string): real official URL to the company careers or internship page (e.g. careers.google.com, careers.microsoft.com, internshala.com, linkedin.com/jobs etc.)
   - skills (array of strings): 3-5 relevant skills
   - is_filled (boolean): always false for new listings
   - is_summer (boolean): true if it is a summer internship program
   - description (string): one sentence max 100 chars describing the role

2. "companies": array of 5 major companies currently known for hiring interns in the given interest areas. Each object must have:
   - name (string)
   - industry (string)
   - reason (string): one sentence on why they are great for interns
   - link (string): real careers page URL

Important rules:
- Prioritise real, well-known companies: Google, Microsoft, Amazon, Meta, Goldman Sachs, McKinsey, Deloitte, Zerodha, CRED, Flipkart, Infosys, TCS, HDFC Bank, Zomato, Swiggy, Razorpay, BYJU's, Unacademy, Internshala, AngelList.
- Include at least 2-3 summer internship programs (is_summer: true).
- Mix remote and in-person locations.
- Mix paid and unpaid stipends.
- All apply_link values must be real, publicly accessible URLs.
- Return ONLY valid JSON. No markdown, no backticks, no explanation text."""

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model='gemini-flash-latest',
                    contents=prompt,
                )
                break
            except Exception as e:
                print(f"Retry {attempt+1} failed: {e}")
                if attempt < 2:
                    time.sleep(2)
                    continue
                # If all retries fail, fall back to static data
                print("All Gemini API retries failed. Serving fallback internships.")
                return jsonify({
                    "internships": FALLBACK_INTERNSHIPS,
                    "companies": FALLBACK_COMPANIES,
                    "is_fallback": True
                }), 200
        
        text = response.text
        if text.startswith("```json"):
            text = text.split("```json")[1]
        if text.startswith("```"):
             text = text.split("```")[1]
        if "```" in text:
             text = text.split("```")[0]
             
        text = text.strip()
        parsed_data = json.loads(text)

        # Filter out past-deadline internships before sending to client
        if "internships" in parsed_data:
            valid_internships = []
            today = datetime.now()
            for item in parsed_data["internships"]:
                if not item.get("deadline"):
                    valid_internships.append(item)
                    continue
                
                try:
                    # Clean ISO format if Z is missing
                    dl_str = item["deadline"].replace("Z", "+00:00")
                    deadline_date = datetime.fromisoformat(dl_str)
                    # Use naive datetime comparison
                    if deadline_date.replace(tzinfo=None) >= today:
                        valid_internships.append(item)
                except ValueError:
                    # If date is completely malformed, let it through as rolling or handle it gracefully
                    valid_internships.append(item)
                    
            parsed_data["internships"] = valid_internships

        # Cache the result
        cache[cache_key] = {"data": parsed_data, "time": time.time()}

        return jsonify(parsed_data), 200

    except Exception as e:
        print("Gemini API error:", str(e))
        # Final safety fallback for parsing errors or unexpected crashes
        return jsonify({
            "internships": FALLBACK_INTERNSHIPS,
            "companies": FALLBACK_COMPANIES,
            "is_fallback": True,
            "error_detail": str(e)
        }), 200
