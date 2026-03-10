from flask import Flask, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>JSS Water Service</title>
        <style>
            body{
                font-family: Arial;
                text-align:center;
                background:#f2f6ff;
                padding-top:80px;
            }
            h1{color:#1b4fff;}
            .box{
                background:white;
                padding:30px;
                width:350px;
                margin:auto;
                border-radius:10px;
                box-shadow:0 0 10px rgba(0,0,0,0.1);
            }
            .btn{
                display:inline-block;
                margin-top:20px;
                padding:12px 25px;
                background:#1b4fff;
                color:white;
                text-decoration:none;
                border-radius:6px;
            }
        </style>
    </head>
    <body>

        <div class="box">
            <h1>💧 JSS Water Service</h1>
            <p>Server Status : Running ✅</p>
            <p>Version : 1.0</p>
            
            <p>App ID : 1234-5678</p>

            <a class="btn" href="/static/jss_water_service.apk">⬇ Download APK</a>
        </div>

    </body>
    </html>
    """)

@app.route("/download")
def download():
    return '<a href="/static/jss_water_service.apk">Click here to download APK</a>'
    
     
@app.route("/status")
def status():
    return "Server Running Perfectly ,u can use your project"

if __name__ == "__main__":
    app.run(port=5123)
