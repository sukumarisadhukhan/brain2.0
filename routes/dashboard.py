from flask import Blueprint, render_template

from services.task_service import get_pending_tasks


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
def dashboard():
    tasks = get_pending_tasks()

    return render_template(
        "dashboard.html",
        tasks=tasks
    )