from flask import Blueprint, request, jsonify
from math import sqrt

from app import db
from app.models.strokes_gained import StrokesGainedBaseline

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze-shot', methods=['POST'])
def analyze_shot():
    data = request.get_json()

    start = data.get("start_coord")
    end = data.get("end_coord")
    lie = data.get("lie", "fairway")
    user_hcp = data.get("handicap_index", 10)

    # Calculate shot distance in yards (simple Euclidean for now)
    def haversine_distance(lat1, lon1, lat2, lon2):
        from math import radians, sin, cos, sqrt, atan2
        R = 6371000  # meters
        phi1, phi2 = radians(lat1), radians(lat2)
        dphi = radians(lat2 - lat1)
        dlambda = radians(lon2 - lon1)
        a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c / 0.9144  # yards

    shot_distance = haversine_distance(start["lat"], start["lng"], end["lat"], end["lng"])

    # Simulated baselines (replace with db query in production)
    # PGA: 2.82 strokes from 160y in fairway
    # User avg: 3.14 (for 10 HCP)
    pga_baseline = 2.82
    user_baseline = 3.14

    # Assume this shot ended the hole (putting handled separately later)
    actual_strokes = 1.0  # for now, just one-shot estimation

    sg_user = user_baseline - actual_strokes
    sg_vs_pga = pga_baseline - actual_strokes

    return jsonify({
        "shot_distance": round(shot_distance, 1),
        "strokes_gained_user": round(sg_user, 2),
        "strokes_gained_vs_pga": round(sg_vs_pga, 2),
        "pga_expected": pga_baseline,
        "user_expected": user_baseline,
        "notes": "Aim slightly right to avoid bunker short left."
    })
