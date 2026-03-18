from flask import Blueprint, request, jsonify, session
from ..models.user_model import UserModel

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    age = data.get('age')
    skills = data.get('skills', '')

    if not username or not password or not age:
        return jsonify({"message": "Missing required fields"}), 400

    if UserModel.get_user_by_username(username):
        return jsonify({"message": "User already exists"}), 400

    if UserModel.create_user(username, password, int(age), skills):
        return jsonify({"message": "User registered successfully"}), 201
    else:
        return jsonify({"message": "Registration failed"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = UserModel.get_user_by_username(username)
    if user and check_password_hash(user['password_hash'], password):
        session['user_id'] = user['id']
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user['id'],
                "username": user['username'],
                "age": user['age']
            }
        }), 200
    
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out"}), 200

@auth_bp.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized"}), 401
    
    data = request.json
    age = data.get('age')
    skills = data.get('skills')

    if not age and not skills:
        return jsonify({"message": "Nothing to update"}), 400

    if UserModel.update_user(session['user_id'], age=age, skills=skills):
        return jsonify({"message": "Profile updated successfully"}), 200
    else:
        return jsonify({"message": "Update failed"}), 500

from werkzeug.security import check_password_hash