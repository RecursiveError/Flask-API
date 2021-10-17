from extension.database import db
from models.luminosidade import Luminosidade
from models.temperatura import Temperatura

def create_db():
    db.create_all()


def drop_db():
    db.drop_all()

def populate_db():
    data = [
        Luminosidade(0, "0000-00-00", "00:00:00"),
        Temperatura(0, "0000-00-00", "00:00:00"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()

def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
