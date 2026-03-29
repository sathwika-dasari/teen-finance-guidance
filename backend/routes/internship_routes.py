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


@internship_bp.route('/', methods=['POST'])
def get_internships():
    try:
        data = request.get_json()
        interests = data.get('interests', [])
        
        if not interests:
            interests_str = "Technology & Fintech, Finance & Banking"
        else:
            interests_str = ", ".join(interests)

        # We will attempt to call Gemini using urllib to avoid missing dependency issues
        gemini_api_key = os.environ.get('GEMINI_API_KEY')
        
        # In case it's not set in os.environ but we want to fail gracefully
        if not gemini_api_key:
            print("GEMINI_API_KEY not found in environment. Using fallback data.")
            return jsonify({
                "internships": FALLBACK_INTERNSHIPS,
                "companies": FALLBACK_COMPANIES
            }), 200

        prompt = f"""
        You are an expert career advisor.
        Based on the user's interests: [{interests_str}], provide a JSON output containing two lists:
        1. "internships": List 8 real internship opportunities for teenagers and young adults (aged 16-22). 
           For each internship include: 
           - "company" (string)
           - "role" (string title)
           - "stipend" (string, e.g. '₹8,000' or 'Unpaid')
           - "duration" (string, e.g. '2 months')
           - "location" (string, Remote or City)
           - "skills" (list of strings)
           - "apply_link" (string URL)
           - "deadline" (string)
        2. "companies": List 6 top companies hiring in these fields that are good for teens.
           For each company include:
           - "name" (string)
           - "industry" (string)
           - "reason" (string, why it's good for teens)
           - "link" (string careers page URL link)

        Return ONLY a valid JSON object with the keys "internships" and "companies". Do not wrap it in markdown codeblocks.
        """

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"response_mime_type": "application/json"}
        }

        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        
        with urllib.request.urlopen(req, timeout=15) as response:
            result = json.loads(response.read().decode('utf-8'))
            
            # Parse gemini text
            text_response = result['candidates'][0]['content']['parts'][0]['text']
            
            # Clean up potential markdown formatting 
            if text_response.startswith('```json'):
                text_response = text_response[7:-3]
            elif text_response.startswith('```'):
                text_response = text_response[3:-3]
                
            parsed_data = json.loads(text_response)
            
            return jsonify({
                "internships": parsed_data.get("internships", FALLBACK_INTERNSHIPS),
                "companies": parsed_data.get("companies", FALLBACK_COMPANIES)
            }), 200

    except Exception as e:
        print(f"Error calling Gemini or parsing: {e}")
        # Always fallback on error
        return jsonify({
            "internships": FALLBACK_INTERNSHIPS,
            "companies": FALLBACK_COMPANIES
        }), 200
