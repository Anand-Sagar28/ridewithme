from flask import Flask

from app.db import close_db
from app.blueprints.rides.admin_routes import admin_bp
from app.blueprints.auth.routes import auth_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    from app.blueprints.rides.routes import rides_bp
    app.register_blueprint(rides_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.teardown_appcontext(close_db)

    return app
