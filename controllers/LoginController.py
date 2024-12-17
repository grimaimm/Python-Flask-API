from flask import jsonify, request
from config import db
from models.UserModel import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta


# Method POST - Login /api/login
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return (
            jsonify({"status": "error", "message": "Invalid username or password"}),
            401,
        )

    access_token = create_access_token(
        identity=username, expires_delta=timedelta(hours=1)
    )
    return (
        jsonify(
            {
                "status": "success",
                "message": "Login successful",
                "access_token": access_token,
            }
        ),
        200,
    )
