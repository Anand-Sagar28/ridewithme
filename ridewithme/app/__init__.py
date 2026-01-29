from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    from app.blueprints.rides.routes import rides_bp
    app.register_blueprint(rides_bp)

    return app
