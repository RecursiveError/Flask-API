from extension.database import db

class Temperatura (db.Model):
    __tablename__ = "temperatura"
    id   = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Date)
    hora = db.Column(db.Time)
    temperatura  = Column(db.Integer)

    def __init__(self, temperatura, data, hora):
        self.temperatura = temperatura
        self.data = data
        self.hora = hora
