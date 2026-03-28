from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.config import Config
from backend.routes.auth_routes import auth_bp
from backend.routes.recommendation import recommend_bp
from backend.routes.dashboard_routes import dashboard_bp
import os

app = Flask(__name__, static_folder='../frontend')
app.config.from_object(Config)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(recommend_bp, url_prefix='/api/recommendation')
app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')

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

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
