from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# ============================================================
# IDENTITY
# ============================================================

class Identity(db.Model):
    __tablename__ = "identities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    icon = db.Column(
        db.String(20),
        nullable=True
    )

    active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ============================================================
# GOAL
# ============================================================

class Goal(db.Model):
    __tablename__ = "goals"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    deadline = db.Column(
        db.DateTime,
        nullable=True
    )

    status = db.Column(
        db.String(20),
        default="active"
    )

    identity_id = db.Column(
        db.Integer,
        db.ForeignKey("identities.id"),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    identity = db.relationship(
        "Identity",
        backref="goals"
    )


# ============================================================
# PROJECT
# ============================================================

class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    deadline = db.Column(
        db.DateTime,
        nullable=True
    )

    status = db.Column(
        db.String(20),
        default="active"
    )

    goal_id = db.Column(
        db.Integer,
        db.ForeignKey("goals.id"),
        nullable=True
    )

    identity_id = db.Column(
        db.Integer,
        db.ForeignKey("identities.id"),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    goal = db.relationship(
        "Goal",
        backref="projects"
    )

    identity = db.relationship(
        "Identity",
        backref="projects"
    )


# ============================================================
# TASK
# ============================================================

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    deadline = db.Column(
        db.DateTime,
        nullable=True
    )

    estimated_minutes = db.Column(
        db.Integer,
        nullable=True
    )

    priority = db.Column(
        db.Integer,
        default=3
    )

    status = db.Column(
        db.String(20),
        default="pending"
    )

    # Identity relationship
    identity_id = db.Column(
        db.Integer,
        db.ForeignKey("identities.id"),
        nullable=True
    )

    identity = db.relationship(
        "Identity",
        backref="tasks"
    )

    # Project relationship
    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=True
    )

    project = db.relationship(
        "Project",
        backref="tasks"
    )

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


# ============================================================
# TIME BLOCK
# ============================================================

class TimeBlock(db.Model):
    __tablename__ = "time_blocks"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    start_time = db.Column(
        db.DateTime,
        nullable=False
    )

    end_time = db.Column(
        db.DateTime,
        nullable=False
    )

    block_type = db.Column(
        db.String(30),
        default="task"
    )

    task_id = db.Column(
        db.Integer,
        db.ForeignKey("tasks.id"),
        nullable=True
    )

    task = db.relationship(
        "Task",
        backref="time_blocks"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ============================================================
# DATABASE HELPERS
# ============================================================

def initialize_database(app):
    """
    Create all database tables if they don't already exist.
    """

    db.init_app(app)

    with app.app_context():
        db.create_all()