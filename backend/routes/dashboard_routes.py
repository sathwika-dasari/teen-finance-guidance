from flask import Blueprint, request, jsonify, session
from ..models.progress_model import ProgressModel

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/progress', methods=['GET'])
def get_progress():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    progress = ProgressModel.get_user_progress(user_id)
    return jsonify(progress), 200

@dashboard_bp.route('/update_progress', methods=['POST'])
def update_progress():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401

    data = request.json
    module_name = data.get('module_name')
    status = data.get('status')
    score = data.get('score', 0)

    if not module_name or not status:
        return jsonify({"message": "Missing fields"}), 400

    ProgressModel.update_progress(user_id, module_name, status, score)
    return jsonify({"message": "Progress updated"}), 200
