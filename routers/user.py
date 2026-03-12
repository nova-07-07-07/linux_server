from flask import Blueprint

user_bp = Blueprint("user", __name__, url_prefix="/routers/user")

@user_bp.route("/")
def user_home():
    return "User Router Working"

@user_bp.route("/profile")
def profile():
    return "User Profile Page"