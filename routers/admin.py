from flask import Blueprint

admin_bp = Blueprint("admin", __name__, url_prefix="/routers/admin")

@admin_bp.route("/")
def admin_home():
    return "Admin Router Working"

@admin_bp.route("/dashboard")
def dashboard():
    return "Admin Dashboard"