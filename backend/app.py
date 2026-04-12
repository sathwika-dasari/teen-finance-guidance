import os
from dotenv import load_dotenv

# Load .env variables before anything else
load_dotenv()

from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from backend.config import Config
from backend.routes.auth_routes import auth_bp
from backend.routes.recommendation import recommend_bp
from backend.routes.dashboard_routes import dashboard_bp
from backend.routes.internship_routes import internship_bp
from backend.routes.job_routes import job_bp
from backend.routes.learning_routes import learning_bp
from backend.routes.chat_routes import chat_bp
from backend.models.job_model import JobModel

from backend.extensions import limiter

app = Flask(__name__, static_folder='../frontend')
app.config.from_object(Config)

# Security & Middleware
CORS(app)
csrf = CSRFProtect(app)
limiter.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(recommend_bp, url_prefix='/api/recommendation')
app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
app.register_blueprint(internship_bp, url_prefix='/api/internships')
app.register_blueprint(job_bp, url_prefix='/api/jobs')
app.register_blueprint(learning_bp, url_prefix='/api/learning')
app.register_blueprint(chat_bp, url_prefix='/api')

# Seed jobs
with app.app_context():
    JobModel.seed_sample_jobs()

# CSRF Token endpoint for AJAX apps
@app.route('/api/csrf_token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

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

@app.route('/budget_simulator')
def serve_budget_simulator():
    return send_from_directory(app.static_folder, 'screens/budget_simulator.html')

@app.route('/guardian_dashboard')
def serve_guardian_dashboard():
    return send_from_directory(app.static_folder, 'screens/guardian_dashboard.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)

