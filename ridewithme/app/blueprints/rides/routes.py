from flask import Blueprint, render_template
from .services import list_rides
from flask import session, redirect, url_for
from .services import join_ride, get_ride_by_id

rides_bp = Blueprint("rides", __name__)

@rides_bp.route("/rides/<int:ride_id>")
def ride_detail(ride_id):
    ride = get_ride_by_id(ride_id)
    return render_template("ride_detail.html", ride=ride)

@rides_bp.route("/rides/<int:ride_id>/join", methods=["POST"])
def join(ride_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("auth.login"))

    success, error = join_ride(user_id, ride_id)
    if not success:
        return error, 400

    return redirect(url_for("rides.ride_detail", ride_id=ride_id))


@rides_bp.route("/")
def home():
    rides = list_rides()
    return render_template("home.html", rides=rides)
