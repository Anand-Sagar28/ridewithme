from flask import Blueprint, render_template

rides_bp = Blueprint("rides", __name__)

@rides_bp.route("/")
def home():
    rides = [
        {
            "title": "Morning City Ride",
            "start_location": "Park",
            "end_location": "Beach",
            "start_datetime": "2026-02-01 06:00",
            "leader_name": "Alex",
            "available_slots": 5
        }
    ]
    return render_template("home.html", rides=rides)
