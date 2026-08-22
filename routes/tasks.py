from flask import Blueprint, render_template, request, redirect, url_for

from services.task_service import create_task, complete_task
from services.identity_service import get_active_identities


tasks_bp = Blueprint(
    "tasks",
    __name__,
    url_prefix="/tasks"
)


@tasks_bp.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form["title"]

        description = request.form.get("description")

        priority = int(
            request.form.get("priority", 3)
        )

        estimated_minutes = request.form.get(
            "estimated_minutes"
        )

        if estimated_minutes:
            estimated_minutes = int(
                estimated_minutes
            )
        else:
            estimated_minutes = None

        deadline = request.form.get("deadline")

        identity_id = request.form.get("identity_id")

        if identity_id:
            identity_id = int(identity_id)
        else:
            identity_id = None

        create_task(
            title=title,
            description=description,
            deadline=deadline,
            estimated_minutes=estimated_minutes,
            priority=priority,
            identity_id=identity_id
        )

        return redirect(
            url_for("dashboard.dashboard")
        )

    identities = get_active_identities()

    return render_template(
        "create_task.html",
        identities=identities
    )


@tasks_bp.route(
    "/complete/<int:task_id>",
    methods=["POST"]
)
def complete(task_id):

    complete_task(task_id)

    return redirect(
        url_for("dashboard.dashboard")
    )