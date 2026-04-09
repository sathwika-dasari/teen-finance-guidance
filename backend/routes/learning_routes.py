from flask import Blueprint, jsonify, request, session
from ..models.user_model import UserModel
from ..models.progress_model import ProgressModel
from ..models.gamification_model import GamificationModel
from ..services.lesson_content import LESSON_DATA
from google import genai
import os
import json

learning_bp = Blueprint('learning', __name__)

STRUCTURED_PATH = [
    {
        "tier": "Beginner",
        "description": "Master the fundamentals of personal finance.",
        "lessons": [
            {"id": "budgeting_101", "title": "Budgeting Basics", "icon": "fa-wallet"},
            {"id": "intro_finance", "title": "Needs vs Wants", "icon": "fa-scale-balanced"},
            {"id": "saving_money", "title": "Saving Money", "icon": "fa-piggy-bank"},
            {"id": "basic_banking", "title": "Basic Banking", "icon": "fa-building-columns"}
        ]
    },
    {
        "tier": "Intermediate",
        "description": "Protect your assets and grow your digital wealth.",
        "lessons": [
            {"id": "digital_payments", "title": "Digital Payments", "icon": "fa-mobile-screen-button"},
            {"id": "scam_prevention", "title": "Avoiding Scams", "icon": "fa-shield-halved"},
            {"id": "understanding_credit", "title": "Understanding Credit", "icon": "fa-credit-card"},
            {"id": "side_income", "title": "Side Income Basics", "icon": "fa-money-bill-trend-up"}
        ]
    },
    {
        "tier": "Advanced (18+)",
        "description": "Build generational wealth and secure your future.",
        "lessons": [
            {"id": "investing_stocks", "title": "Investing Basics", "icon": "fa-chart-pie"},
            {"id": "mutual_funds", "title": "Mutual Funds", "icon": "fa-chart-line"},
            {"id": "freelance_dev_lesson", "title": "Freelancing Income", "icon": "fa-laptop-code"},
            {"id": "risk_management", "title": "Risk Management", "icon": "fa-umbrella"}
        ]
    }
]

@learning_bp.route('/path', methods=['GET'])
def get_learning_path():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    # Get user progress to calculate locks
    progress_records = ProgressModel.get_user_progress(user_id)
    completed_modules = {p['module_name'] for p in progress_records if p['status'] == 'completed'}
    
    # Get gamification stats
    stats = GamificationModel.get_user_stats(user_id)

    # Calculate locks (simple progressive locking: a lesson is unlocked if the previous one is completed)
    # Actually, Duolingo unlocks the next node. For this demo, let's unlock the first lesson of a tier, 
    # and subsequent ones only if previous is completed.
    
    response_tiers = []
    global_unlocked = True # First lesson is always unlocked
    
    for tier in STRUCTURED_PATH:
        tier_data = {
            "tier": tier["tier"],
            "description": tier["description"],
            "lessons": []
        }
        
        for lesson in tier["lessons"]:
            is_completed = lesson["id"] in completed_modules
            
            lesson_node = {
                "id": lesson["id"],
                "title": lesson["title"],
                "icon": lesson["icon"],
                "status": "completed" if is_completed else ("unlocked" if global_unlocked else "locked")
            }
            tier_data["lessons"].append(lesson_node)
            
            # If a lesson isn't completed, the next one is locked
            if not is_completed:
                global_unlocked = False
                
        response_tiers.append(tier_data)

    return jsonify({
        "path": response_tiers,
        "gamification": stats
    }), 200

@learning_bp.route('/complete_lesson', methods=['POST'])
def complete_lesson():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.json
    module_name = data.get('module_name')
    score = data.get('score', 0)
    
    if not module_name:
        return jsonify({"message": "Module name is required"}), 400
        
    # Update progress
    ProgressModel.update_progress(user_id, module_name, 'completed', score)
    
    # Award gamification XP (e.g., 50 XP per standard lesson, + bonus for score)
    earned_xp = 50 + int((score / 100) * 50)
    new_stats = GamificationModel.add_xp_and_update_streak(user_id, earned_xp)
    
    return jsonify({
        "message": "Lesson completed successfully!",
        "earned_xp": earned_xp,
        "new_stats": new_stats
    }), 200

@learning_bp.route('/generate_lesson', methods=['POST'])
def generate_lesson():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401
        
    data = request.json
    interest = data.get('interest', 'Personal Finance')
    skill_level = data.get('skill_level', 'Beginner')
    
    # Load API key securely from environment — never hardcode keys
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return jsonify({"message": "Server configuration error: GEMINI_API_KEY is not set."}), 503

    client = genai.Client(api_key=api_key)
    
    system_prompt = f"""
    You are an expert EdTech finance instructor creating interactive lessons for teenagers.
    Create a personalized micro-lesson focusing on {interest} for a {skill_level} level student.
    
    The lesson MUST be strictly formatted as a JSON object with this exact schema:
    {{
        "title": "A catchy title for the lesson",
        "image": "../assets/intro_finance.png", 
        "topics": [
            {{
                "title": "Topic 1 (e.g. Concept Explanation)",
                "content": "Clear, engaging explanation using simple language."
            }},
            {{
                "title": "Topic 2 (e.g. Real-Life Example)",
                "content": "A highly relatable real-world example."
            }},
            {{
                "title": "Topic 3 (e.g. Safety/Pro Tip)",
                "content": "Important highlights or safety tips."
            }}
        ],
        "quiz": [
            {{
                "q": "A multiple choice question checking understanding?",
                "a": ["Option 1", "Option 2", "Option 3"],
                "correct": 0
            }},
            {{
                "q": "Another multiple choice question?",
                "a": ["Wrong", "Right", "Wrong"],
                "correct": 1
            }}
        ]
    }}
    
    Ensure the JSON is perfectly valid and completely enclosed within ```json and ``` markdown markers.
    Do NOT include any text outside the JSON block.
    """
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-flash-latest',
                contents=system_prompt,
            )
            break
        except Exception as e:
            if attempt < 2:
                import time
                time.sleep(2)
                continue
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                return jsonify({"message": "Our AI teacher is taking a short break (quota limit). Please try again in a few moments!"}), 503
            print(f"Error generating AI lesson after retries: {e}")
            return jsonify({"message": "Failed to generate lesson via AI"}), 500

    try:
        text = response.text
        
        # Parse JSON from markdown blocks
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
            
        custom_lesson = json.loads(text)
        custom_lesson["id"] = "ai_generated_lesson"
        
        return jsonify(custom_lesson), 200
        
    except Exception as e:
        print(f"Error parsing AI lesson: {e}")
        return jsonify({"message": "Failed to generate lesson via AI"}), 500
