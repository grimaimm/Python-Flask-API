from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# Method GET - Auth Protected /api/auth-protected
@jwt_required()
def auth_protected():
  current_user = get_jwt_identity()
  return jsonify(logged_in_as=current_user), 200