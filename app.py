from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/status")
def status():
    return "Server Running Perfectly , u can use your project"

if __name__ == "__main__":
    app.run(port=5123)