from datetime import datetime

from models.models import db, Task


def create_task(
    title,
    description=None,
    deadline=None,
    estimated_minutes=None,
    priority=3
):
    """Create and save a new task."""

    if deadline:
        deadline = datetime.fromisoformat(deadline)

    task = Task(
        title=title,
        description=description,
        deadline=deadline,
        estimated_minutes=estimated_minutes,
        priority=priority
    )

    db.session.add(task)
    db.session.commit()

    return task


def get_all_tasks():
    """Return all tasks, ordered by deadline."""

    return Task.query.order_by(
        Task.deadline.asc()
    ).all()


def get_pending_tasks():
    """Return incomplete tasks, ordered by deadline."""

    return Task.query.filter_by(
        status="pending"
    ).order_by(
        Task.deadline.asc()
    ).all()


def get_task(task_id):
    """Return a task by ID."""

    return db.session.get(Task, task_id)


def complete_task(task_id):
    """Mark a task as completed."""

    task = db.session.get(Task, task_id)

    if task is None:
        return None

    task.status = "completed"
    task.completed_at = datetime.utcnow()

    db.session.commit()

    return task


def delete_task(task_id):
    """Delete a task."""

    task = db.session.get(Task, task_id)

    if task is None:
        return None

    db.session.delete(task)
    db.session.commit()

    return task