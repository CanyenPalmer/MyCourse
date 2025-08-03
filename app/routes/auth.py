from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if User.query.filter_by(email=email).first():
        return jsonify({ "error": "User already exists" }), 400

    hashed_pw = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({ "user_id": new_user.id })

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        return jsonify({ "user_id": user.id })
    return jsonify({ "error": "Invalid credentials" }), 401
