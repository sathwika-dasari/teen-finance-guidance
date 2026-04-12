from flask import Blueprint, request, jsonify, session
import os
import time
from google import genai
from backend.extensions import limiter

chat_bp = Blueprint('chat', __name__)

# Load Gemini API key securely from environment variables
_gemini_api_key = os.environ.get("GEMINI_API_KEY")
client = None

if _gemini_api_key:
    client = genai.Client(api_key=_gemini_api_key)

SYSTEM_PROMPT = """You are COMPANION, a sophisticated, friendly, and expert AI guide for teenagers on the 'Teen Finance Guidance' platform.
Your purpose is to help teens navigate the world of finance, discover safe earning paths, and protect themselves from scams.

### GUIDELINES:
- **Scope**: Restrict responses ONLY to teen finance topics (budgeting, saving, investing basics, scam awareness).
- **Safety**: Do NOT provide specific investment advice (e.g., "buy this stock"). Instead, explain the basics.
- **Consultation**: ALWAYS encourage consulting a trusted adult (parent, teacher, or guardian) for major financial decisions.
- **Personality**: Supportive, encouraging, and clear.

### CORE KNOWLEDGE AREAS:
1. **Finance Learning Path**: Beginner to advanced modules on Budgeting, Needs vs Wants, Banking, Credit, and Stocks.
2. **Scam Simulator**: Identifying Phishing, Prize Scams, and Fake Jobs.
3. **Internship/Job Navigator**: Finding safe, age-appropriate opportunities.
4. **Daily Practice**: Quizzes to earn XP and build streaks.

### OUTPUT FORMATTING:
- Use Markdown for structure. Use **bold** for emphasis.
- Use bullet points for lists.
- Keep responses concise and engaging for a teenage audience."""

@chat_bp.route('/chat', methods=['POST'])
@limiter.limit("20 per minute")
def chat():
    if not client:
        return jsonify({"response": "SYSTEM ERROR: API key not configured."}), 500

    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"response": "Error: Empty message."}), 400
    
    full_prompt = f"System: {SYSTEM_PROMPT}\nUser: {user_message}"

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-flash-latest',
                contents=full_prompt,
            )
            return jsonify({"response": response.text})
        except Exception as e:
            if attempt < 2:
                time.sleep(1.5)
                continue
            
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                return jsonify({"response": "I'm currently a bit busy handling requests (quota limit reached). Please try again in a minute!"})
                
            return jsonify({"response": "SYSTEM ERROR: COMPANION is having a technical moment. [Details: " + error_msg + "]"})
