from flask import Blueprint
from controllers.AuthController import *
from controllers.LoginController import *

auth_bp = Blueprint("auth_bp", __name__)

auth_bp.route("/api/login", methods=["POST"])(login)
auth_bp.route("/api/auth-protected", methods=["GET"])(auth_protected)