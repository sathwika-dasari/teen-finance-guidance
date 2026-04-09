import os
from dotenv import load_dotenv

# Load .env variables before anything else (no-op if running in production with real env vars)
load_dotenv()

from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.config import Config
from backend.routes.auth_routes import auth_bp
from backend.routes.recommendation import recommend_bp
from backend.routes.dashboard_routes import dashboard_bp
from backend.routes.internship_routes import internship_bp
from backend.routes.job_routes import job_bp
from backend.routes.learning_routes import learning_bp
from backend.models.job_model import JobModel

app = Flask(__name__, static_folder='../frontend')
app.config.from_object(Config)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(recommend_bp, url_prefix='/api/recommendation')
app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
app.register_blueprint(internship_bp, url_prefix='/api/internships')
app.register_blueprint(job_bp, url_prefix='/api/jobs')
app.register_blueprint(learning_bp, url_prefix='/api/learning')

# Seed jobs
with app.app_context():
    JobModel.seed_sample_jobs()

# Serve Static Files
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/login')
@app.route('/register')
def serve_auth():
    return send_from_directory(app.static_folder, 'screens/login.html')

@app.route('/dashboard')
def serve_dashboard():
    return send_from_directory(app.static_folder, 'screens/dashboard.html')

@app.route('/home')
def serve_home():
    return send_from_directory(app.static_folder, 'screens/home.html')

@app.route('/profile')
def serve_profile():
    return send_from_directory(app.static_folder, 'screens/profile.html')

@app.route('/lessons')
def serve_lessons():
    return send_from_directory(app.static_folder, 'screens/lessons.html')

@app.route('/learning_path')
def serve_learning_path():
    return send_from_directory(app.static_folder, 'screens/learning_path.html')

@app.route('/daily')
def serve_daily():
    return send_from_directory(app.static_folder, 'screens/daily_practice.html')

@app.route('/parttime')
def serve_parttime():
    return send_from_directory(app.static_folder, 'screens/parttime.html')

@app.route('/internships')
def serve_internships():
    return send_from_directory(app.static_folder, 'screens/jobs.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

from google import genai
from flask import request, jsonify
import time

# 🔑 Load Gemini API key securely from environment variables (.env file)
_gemini_api_key = os.environ.get("GEMINI_API_KEY")
if not _gemini_api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. "
        "Please add it to your .env file: GEMINI_API_KEY=your_key_here"
    )
client = genai.Client(api_key=_gemini_api_key)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"response": "Error: Empty message."})
    
    # Dynamic context for COMPANION AI
    system_prompt = f"""You are COMPANION, a sophisticated, friendly, and expert AI guide for teenagers on the 'Teen Finance Guidance' platform.
Your purpose is to help teens navigate the world of finance, discover safe earning paths, and protect themselves from scams.

### YOUR PERSONALITY:
- Supportive, encouraging, and easy to talk to (like a mentor/big sibling).
- Clear, concise, and structured in your explanations.
- Highly dedicated to safety and financial literacy.

### CORE KNOWLEDGE AREAS:
1. **Finance Learning Path**: We offer beginner to advanced modules on Budgeting, Needs vs Wants, Banking, Credit, and Stocks. Guided learning is at '/learning_path'.
2. **Scam Simulator**: An interactive game where users learn to identify Phishing, Prize Scams, and Fake Jobs. Strongly recommend users visit this under the 'Avoiding Scams' module.
3. **Internship/Job Navigator**: Located at '/internships'. It provides both AI-generated live listings and static opportunities.
4. **Daily Practice**: Daily quizzes to earn XP and build streaks ('/daily').
5. **Skill Guidance**: Suggesting ways to earn safely (Freelance writing, Design, Tutoring, Selling crafts).

### CONVERSATIONAL RULES:
- **Greetings**: Respond warmly to "hi", "hello", or casual talk.
- **System Help**: If asked "how to use this app" or similar, explain the side navigation and the features above step-by-step.
- **Job/Internship Guidance**:
    - Understand if they want "Writing", "Design", "Tech", or "General" roles.
    - provide 3-5 REAL external links (LinkedIn, Internshala, Unstop, etc.) but ALWAYS wrap them in educational advice (e.g., "Build a portfolio first").
    - MANDATORY SAFETY WARNING: Remind them to NEVER pay fees for jobs, verify employers on official sites, and involve parents for offline roles.
- **Motivation**: Encourage them to stay consistent with their learning path to earn badges and levels.

### OUTPUT FORMATTING:
- Use Markdown for structure. Use **bold** for emphasis. Use [Link Text](URL) for links.
- Use bullet points for lists.
- Avoid very long paragraphs."""
    
    full_prompt = f"System: {system_prompt}\nUser: {user_message}"

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
            
            # Detect 429 specifically for a better message
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                return jsonify({"response": "I'm currently a bit busy handling requests (quota limit reached). Please try again in a minute, or check out our **Internships** section for some great opportunities while you wait!"})
                
            return jsonify({"response": "SYSTEM ERROR: COMPANION is having a technical moment. Please try again. [Details: " + error_msg + "]"})

if __name__ == '__main__':
    import webbrowser
    from threading import Timer

    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")

    # Open browser 1 second after starting
    Timer(1, open_browser).start()
    
    # use_reloader=False prevents opening two browser windows
    app.run(debug=True, port=5000, use_reloader=False)
