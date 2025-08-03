from flask import Blueprint, jsonify

from app import db
from app.models.shot import Shot

summary_bp = Blueprint('summary', __name__)

@summary_bp.route('/round-summary/<int:user_id>', methods=['GET'])
def round_summary(user_id):
    # In production, you'd filter by round_id too
    shots = Shot.query.filter_by(user_id=user_id).all()

    summary = []
    total_sg_user = 0
    total_sg_pga = 0
    total_chips = 0
    total_putts = 0
    total_hazards = 0
    total_penalties = 0
    for idx, shot in enumerate(shots, 1):
        # Placeholder: assume 1 stroke taken and static baselines
        total_chips += shot.chips or 0
        total_putts += shot.putts or 0
        total_hazards += shot.hazards or 0
        total_penalties += shot.penalties or 0        pga_expected = 2.82
        user_expected = 3.14
        actual = 1.0

        sg_user = round(user_expected - actual, 2)
        sg_pga = round(pga_expected - actual, 2)

        total_sg_user += sg_user
        total_sg_pga += sg_pga

        summary.append({
            "shot": idx,
            "club": shot.club,
            "lie": shot.lie,
            "distance": round(((shot.end_x - shot.start_x)**2 + (shot.end_y - shot.start_y)**2)**0.5, 1),
            "sg_user": sg_user,
            "sg_pga": sg_pga
        })

    return jsonify({
        "totals": {
            "chips": total_chips,
            "putts": total_putts,
            "hazards": total_hazards,
            "penalties": total_penalties
        },        "user_id": user_id,
        "total_sg_user": round(total_sg_user, 2),
        "total_sg_pga": round(total_sg_pga, 2),
        "shots": summary
    })
