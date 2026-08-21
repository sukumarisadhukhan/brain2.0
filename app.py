from flask import Flask, render_template
from routes.tasks import tasks_bp
from models.models import db
from routes.dashboard import dashboard_bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///brain.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(tasks_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)