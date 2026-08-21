from datetime import datetime, timedelta

from services.task_service import get_pending_tasks
from services.priority_engine import rank_tasks


def get_today_tasks():
    """Get tasks due today or overdue."""

    tasks = get_pending_tasks()

    now = datetime.now()
    end_of_day = datetime.combine(
        now.date(),
        datetime.max.time()
    )

    today_tasks = []

    for task in tasks:

        if task.deadline is None:
            continue

        if task.deadline <= end_of_day:
            today_tasks.append(task)

    return today_tasks


def calculate_workload(tasks):
    """Calculate total estimated work in minutes."""

    total_minutes = 0

    for task in tasks:
        if task.estimated_minutes:
            total_minutes += task.estimated_minutes

    return total_minutes


def get_daily_plan(available_minutes=300):
    """
    Build a realistic daily plan.

    Higher-priority tasks are selected first
    until available time is exhausted.
    """

    tasks = get_pending_tasks()

    ranked_tasks = rank_tasks(tasks)

    selected = []
    total_minutes = 0

    for task, score in ranked_tasks:

        duration = task.estimated_minutes or 30

        if total_minutes + duration <= available_minutes:

            selected.append(
                (task, score)
            )

            total_minutes += duration

    return {
        "tasks": selected,
        "total_minutes": total_minutes,
        "available_minutes": available_minutes,
        "remaining_minutes":
            available_minutes - total_minutes
    }