from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    deadline = db.Column(db.DateTime, nullable=True)

    estimated_minutes = db.Column(db.Integer, nullable=True)

    priority = db.Column(db.Integer, default=3)
    status = db.Column(db.String(20), default="pending")

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    completed_at = db.Column(
        db.DateTime,
        nullable=True
    )

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"