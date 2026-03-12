from flask import Blueprint, request, jsonify
from db import get_db

user_bp = Blueprint("user", __name__, url_prefix="/routers/user")


@user_bp.route("/register", methods=["POST"])
def register():
    if not request.json:
        return jsonify({"error":"Invalid request"}), 400
    data = request.json

    required = ["userid","name","mob_no","otp"]

    missing = [k for k in required if k not in data]

    if missing:
        return jsonify({"error":"Missing fields","fields":missing}),400

    name = data.get("name")
    role = data.get("role","user")
    profile_pic = data.get("profile_pic","")
    mob_no = data.get("mob_no")
    address = str(data.get("add",[]))
    refimg = str(data.get("refrenceimg",[]))

    conn = get_db()

    

    try:
        otp_row = conn.execute(
        "SELECT * FROM otp_verify WHERE mob_no=? AND otp=? ORDER BY id DESC LIMIT 1",
        (data["mob_no"],data["otp"])
        ).fetchone()

        

        if not otp_row:
            return jsonify({"message":"Invalid OTP ,Enter again"}),400
        
        conn.execute(
        "DELETE FROM otp_verify WHERE id=?",
        (otp_row["id"],)
        )
        conn.execute(
        "INSERT INTO users (userid,name,role,profile_pic,mob_no,address,referenceimg) VALUES (?,?,?,?,?,?,?)",
        (name,role,profile_pic,mob_no,address,refimg)
        )

        conn.commit()

        return jsonify({"message":"success"})

    except Exception as e:
        return jsonify({"message":str(e)})

    finally:
        conn.close()

import random

@user_bp.route("/send_otp", methods=["POST"])
def send_otp():

    data = request.json
    mob_no = data.get("mob_no")

    if not mob_no:
        return jsonify({"message":"mobile number is required"}),400

    otp = str(random.randint(100000,999999))

    conn = get_db()
    conn.execute(
        "INSERT INTO otp_verify (mob_no,otp) VALUES (?,?)",
        (mob_no,otp)
    )
    conn.commit()
    conn.close()

    return jsonify({
        "message":"OTP sent",
        "otp":otp   # remove in production
    })