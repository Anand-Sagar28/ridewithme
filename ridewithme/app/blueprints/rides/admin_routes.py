from flask import Blueprint, render_template, request, redirect, url_for, abort
from .services import add_ride
from flask import current_app

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/rides/new", methods=["GET", "POST"])
def create_ride():
    if not current_app.config.get("ADMIN_MODE"):
        abort(403)

    if request.method == "POST":
        add_ride({
            "title": request.form["title"],
            "description": request.form.get("description"),
            "start_location": request.form["start_location"],
            "end_location": request.form["end_location"],
            "start_datetime": request.form["start_datetime"],
            "max_participants": int(request.form["max_participants"]),
            "leader_name": request.form["leader_name"],
            "leader_contact": request.form["leader_contact"],
        })
        return redirect(url_for("rides.home"))

    return render_template("admin/create_ride.html")
