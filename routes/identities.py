from flask import Blueprint, render_template, request, redirect, url_for

from services.identity_service import (
    create_identity,
    get_active_identities
)


identities_bp = Blueprint(
    "identities",
    __name__,
    url_prefix="/identities"
)


@identities_bp.route("/")
def list_identities():

    identities = get_active_identities()

    return render_template(
        "identities.html",
        identities=identities
    )


@identities_bp.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        name = request.form["name"]

        description = request.form.get(
            "description"
        )

        icon = request.form.get(
            "icon"
        )

        create_identity(
            name=name,
            description=description,
            icon=icon
        )

        return redirect(
            url_for(
                "identities.list_identities"
            )
        )

    return render_template(
        "create_identity.html"
    )