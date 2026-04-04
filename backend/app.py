from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.config import Config
from backend.routes.auth_routes import auth_bp
from backend.routes.recommendation import recommend_bp
from backend.routes.dashboard_routes import dashboard_bp
from backend.routes.internship_routes import internship_bp
import os

app = Flask(__name__, static_folder='../frontend')
app.config.from_object(Config)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(recommend_bp, url_prefix='/api/recommendation')
app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
app.register_blueprint(internship_bp, url_prefix='/api/internships')

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

@app.route('/daily')
def serve_daily():
    return send_from_directory(app.static_folder, 'screens/daily_practice.html')

@app.route('/parttime')
def serve_parttime():
    return send_from_directory(app.static_folder, 'screens/parttime.html')

@app.route('/internships')
def serve_internships():
    return send_from_directory(app.static_folder, 'screens/internships.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

from google import genai
from flask import request, jsonify
import time

# 🔑 Set your API key here
client = genai.Client(api_key="Your api key")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"response": "Error: Empty message."})
    
    # Tactical context for NetraOS
    system_prompt = "You are COMPANION, a tactical visual assistant. Use a concise, tactical, and assertive tone. You are assisting a user in the Teen Finance Guidance platform. Provide helpful, short financial guidance when asked."
    full_prompt = f"System: {system_prompt}\nUser: {user_message}"

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=full_prompt,
            )
            return jsonify({"response": response.text})
        except Exception as e:
            if attempt < 2:
                time.sleep(1.5)
                continue
            return jsonify({"response": "SYSTEM ERROR: BUDDY sensors overloaded. Please try again. [Details: " + str(e) + "]"})

if __name__ == '__main__':
    import webbrowser
    from threading import Timer

    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000/")

    # Open browser 1 second after starting
    Timer(1, open_browser).start()
    
    # use_reloader=False prevents opening two browser windows
    app.run(debug=True, port=5000, use_reloader=False)
