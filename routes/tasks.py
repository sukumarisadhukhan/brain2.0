from flask import Blueprint, render_template, request, redirect, url_for
from services.task_service import create_task, complete_task

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        priority = int(request.form.get("priority", 3))

        estimated_minutes = request.form.get("estimated_minutes")

        if estimated_minutes:
            estimated_minutes = int(estimated_minutes)
        else:
            estimated_minutes = None

        deadline = request.form.get("deadline")

        create_task(
            title=title,
            description=description,
            deadline=deadline,
            estimated_minutes=estimated_minutes,
            priority=priority
        )

        return redirect(url_for("dashboard.dashboard"))

    return render_template("create_task.html")


@tasks_bp.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    complete_task(task_id)
    return redirect(url_for("dashboard.dashboard"))
