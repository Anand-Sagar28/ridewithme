from flask import Blueprint, render_template, request, redirect, url_for, session
from .services import register_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        success, error = register_user(name, email, password)
        if success:
            return redirect(url_for("auth.login"))
        return render_template("auth/register.html", error=error)

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = authenticate_user(email, password)
        if user:
            session["user_id"] = user["id"]
            return redirect(url_for("rides.home"))

        return render_template("auth/login.html", error="Invalid credentials")

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("rides.home"))
