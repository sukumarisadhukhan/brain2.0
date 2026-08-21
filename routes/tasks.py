from flask import Blueprint, render_template, request, redirect, url_for
from services.task_service import create_task, complete_task


tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        priority = int(request.form.get("priority", 3))

        create_task(
            title=title,
            description=description,
            priority=priority
        )

        return redirect(url_for("dashboard.dashboard"))

    return render_template("create_task.html")


@tasks_bp.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    complete_task(task_id)

    return redirect(url_for("dashboard.dashboard"))