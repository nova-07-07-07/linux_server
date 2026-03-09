from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "server running , ok 🔮 1234 5678 91011 "
     
@app.route("/status")
def status():
    return "Server Running Perfectly ,u can use your project"

if __name__ == "__main__":
    app.run(port=5123)
