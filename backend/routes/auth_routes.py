from flask import Blueprint, request, jsonify, session
from ..models.user_model import UserModel

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    age = data.get('age')
    skills = data.get('skills', '')
    role = data.get('role', 'student')

    if not username or not password or not age or not email:
        return jsonify({"message": "Missing required fields (username, password, email, age)"}), 400

    if UserModel.get_user_by_username(username):
        return jsonify({"message": "Username already exists"}), 400
    
    if UserModel.get_user_by_email(email):
        return jsonify({"message": "Email already exists"}), 400

    if UserModel.create_user(username, password, email, int(age), skills, role):
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
        session['role'] = user['role']
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "role": user['role'],
                "age": user['age']
            }
        }), 200
    
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/link_student', methods=['POST'])
def link_student():
    if 'user_id' not in session or session.get('role') != 'guardian':
        return jsonify({"message": "Unauthorized or not a guardian"}), 401
    
    data = request.json
    student_email = data.get('student_email')
    if not student_email:
        return jsonify({"message": "Student email is required"}), 400
        
    success, msg = UserModel.link_guardian(session['user_id'], student_email)
    if success:
        return jsonify({"message": msg}), 200
    else:
        return jsonify({"message": msg}), 400

@auth_bp.route('/linked_students', methods=['GET'])
def get_linked_students():
    if 'user_id' not in session or session.get('role') != 'guardian':
        return jsonify({"message": "Unauthorized or not a guardian"}), 401
        
    students = UserModel.get_linked_students(session['user_id'])
    return jsonify({"students": students}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
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