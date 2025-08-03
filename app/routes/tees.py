from flask import Blueprint, jsonify
from app.models.tee import Tee
from app.models.hole import Hole

tees_bp = Blueprint('tees', __name__)

@tees_bp.route('/tees/<string:course_name>', methods=['GET'])
def get_tees(course_name):
    tees = Tee.query.filter_by(course_name=course_name).all()
    return jsonify([
        {
            "tee_id": t.id,
            "tee_name": t.tee_name,
            "total_yardage": t.total_yardage
        } for t in tees
    ])

@tees_bp.route('/tee/<int:tee_id>/holes', methods=['GET'])
def get_holes_for_tee(tee_id):
    holes = Hole.query.filter_by(tee_id=tee_id).order_by(Hole.hole_number).all()
    return jsonify([
        {
            "hole_number": h.hole_number,
            "yardage": h.yardage,
            "par": h.par
        } for h in holes
    ])
