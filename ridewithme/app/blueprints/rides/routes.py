from flask import Blueprint, render_template, request
from .services import list_rides
from flask import session, redirect, url_for
from .services import join_ride, get_ride_by_id
from flask import request
from .services import simulate_payment
from .services import get_user_code



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

    return redirect(url_for("rides.confirm_join", ride_id=ride_id))


@rides_bp.route("/rides/<int:ride_id>/confirm", methods=["GET", "POST"])
def confirm_join(ride_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        success, error = join_ride(user_id, ride_id)
        if not success:
            return error, 400

        return redirect(url_for("rides.payment", ride_id=ride_id))

    ride = get_ride_by_id(ride_id)
    return render_template("confirm_join.html", ride=ride)

@rides_bp.route("/payment/<int:ride_id>", methods=["GET", "POST"])
def payment(ride_id):
    user_id = session.get("user_id")

    if request.method == "POST":
        ref = simulate_payment(user_id, ride_id)
        code = get_user_code(user_id, ride_id)

        return render_template(
            "payment_success.html",
            code=code
        )

    return render_template("payment.html")



@rides_bp.route("/")
def home():
    rides = list_rides()
    return render_template("home.html", rides=rides)
