from flask import Blueprint, render_template
from .services import list_rides

rides_bp = Blueprint("rides", __name__)

@rides_bp.route("/")
def home():
    rides = list_rides()
    return render_template("home.html", rides=rides)
