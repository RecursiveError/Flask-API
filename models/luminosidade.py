from extension.database import db

class Luminosidade (db_base):
    __tablename__ = "luminosidade"
    id   = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Date)
    hora = db.Column(db.Time)
    lux  = db.Column(db.Integer)

    def __init__(self, lux, data, hora):
        self.lux = lux
        self.data = data
        self.hora = hora


