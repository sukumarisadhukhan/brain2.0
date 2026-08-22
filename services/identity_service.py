from models.models import db, Identity


def create_identity(name, description=None, icon=None):

    identity = Identity(
        name=name,
        description=description,
        icon=icon
    )

    db.session.add(identity)
    db.session.commit()

    return identity


def get_active_identities():

    return Identity.query.filter_by(
        active=True
    ).order_by(
        Identity.name.asc()
    ).all()


def get_identity(identity_id):

    return db.session.get(
        Identity,
        identity_id
    )