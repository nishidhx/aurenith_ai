from flask import Blueprint 
from controllers.user_controller import create_user

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/users", methods=["POST"])(create_user)