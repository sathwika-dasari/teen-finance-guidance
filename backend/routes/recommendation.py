from flask import Blueprint, jsonify, session
from ..models.user_model import UserModel
from ..services.rule_engine import RuleEngine
from ..services.lesson_content import LESSON_DATA

recommend_bp = Blueprint('recommendation', __name__)

@recommend_bp.route('/get_guidance', methods=['GET'])
def get_guidance():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    user = UserModel.get_user_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    recommendations = RuleEngine.get_recommendations(user['age'], user['skills'])
    
    # Add images for dashboard display
    for lesson in recommendations['lessons']:
        lesson['image'] = LESSON_DATA.get(lesson['id'], {}).get('image', '../assets/default.png')

    return jsonify(recommendations), 200

@recommend_bp.route('/get_lesson/<module_id>', methods=['GET'])
def get_lesson(module_id):
    lesson = LESSON_DATA.get(module_id)
    if not lesson:
        return jsonify({"message": "Lesson not found"}), 404
    return jsonify(lesson), 200
