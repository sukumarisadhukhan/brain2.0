from flask import Blueprint, render_template

from services.task_service import get_pending_tasks
from services.priority_engine import rank_tasks
from services.scheduling_engine import get_daily_plan


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
def dashboard():

    tasks = get_pending_tasks()

    ranked_tasks = rank_tasks(tasks)

    daily_plan = get_daily_plan(
        available_minutes=300
    )

    return render_template(
        "dashboard.html",
        ranked_tasks=ranked_tasks,
        daily_plan=daily_plan
    )