from flask import Flask, render_template
from flask_cors import CORS
from routers import user_bp
from db import init_db
from routers.user import user_bp
from routers.admin import admin_bp
import subprocess

# install requirements.txt
# pip install -r requirements.txt
subprocess.call(["pip", "install", "-r", "requirements.txt"])

app = Flask(__name__)
CORS(app)

init_db()

app.register_blueprint(user_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

@app.route("/downlode_app")
def home():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("Signup.html")

@app.route("/status")
def status():
    return "Server Running Perfectly , u can use your project !"

@app.route("/remove_db123")
def remove_db():
    import os
    # ./database.db
    DB = "database.db"
    os.remove(DB)
    return "Database removed successfully"

if __name__ == "__main__":
    app.run(port=5123)