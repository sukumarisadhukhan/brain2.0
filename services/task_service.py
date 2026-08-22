from datetime import datetime

from models.models import db, Task


def create_task(
    title,
    description=None,
    deadline=None,
    estimated_minutes=None,
    priority=3,
    identity_id=None
):

    if deadline:
        deadline = datetime.fromisoformat(deadline)

    task = Task(
        title=title,
        description=description,
        deadline=deadline,
        estimated_minutes=estimated_minutes,
        priority=priority,
        identity_id=identity_id
    )

    db.session.add(task)
    db.session.commit()

    return task


def get_all_tasks():

    return Task.query.order_by(
        Task.deadline.asc()
    ).all()


def get_pending_tasks():

    return Task.query.filter_by(
        status="pending"
    ).order_by(
        Task.deadline.asc()
    ).all()


def get_task(task_id):

    return db.session.get(
        Task,
        task_id
    )


def complete_task(task_id):

    task = db.session.get(
        Task,
        task_id
    )

    if task is None:
        return None

    task.status = "completed"
    task.completed_at = datetime.utcnow()

    db.session.commit()

    return task


def delete_task(task_id):

    task = db.session.get(
        Task,
        task_id
    )

    if task is None:
        return None

    db.session.delete(task)
    db.session.commit()

    return tasks