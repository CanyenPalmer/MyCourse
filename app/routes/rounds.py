from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from app.models.round import Round

rounds_bp = Blueprint('rounds', __name__)

@rounds_bp.route('/rounds/create', methods=['POST'])
def create_round():
    data = request.get_json()
    new_round = Round(
        user_id=data['user_id'],
        course_name=data.get('course_name', 'Unnamed Course'),
        date=datetime.utcnow()
    )
    db.session.add(new_round)
    db.session.commit()
    return jsonify({ "round_id": new_round.id })

@rounds_bp.route('/rounds/<int:user_id>', methods=['GET'])
def list_rounds(user_id):
    rounds = Round.query.filter_by(user_id=user_id).order_by(Round.date.desc()).all()
    return jsonify([
        {
            "round_id": r.id,
            "course_name": r.course_name,
            "date": r.date.strftime('%Y-%m-%d %H:%M')
        } for r in rounds
    ])

from flask import request
from app.models.round import Round

@rounds_bp.route('/rounds/<int:round_id>', methods=['PATCH'])
def rename_round(round_id):
    data = request.get_json()
    round_obj = Round.query.get(round_id)
    if not round_obj:
        return jsonify({"error": "Round not found"}), 404
    round_obj.course_name = data.get("course_name", round_obj.course_name)
    db.session.commit()
    return jsonify({"message": "Round updated"})

@rounds_bp.route('/rounds/<int:round_id>', methods=['DELETE'])
def delete_round(round_id):
    round_obj = Round.query.get(round_id)
    if not round_obj:
        return jsonify({"error": "Round not found"}), 404
    db.session.delete(round_obj)
    db.session.commit()
    return jsonify({"message": "Round deleted"})
