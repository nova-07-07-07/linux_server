from flask import Flask, render_template
from flask_cors import CORS

from routers.user import user_bp
from routers.admin import admin_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

@app.route("/downlode_app")
def home():
    return render_template("index.html")

@app.route("/status")
def status():
    return "Server Running Perfectly , u can use your project !"

if __name__ == "__main__":
    app.run(port=5123)