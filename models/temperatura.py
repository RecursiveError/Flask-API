from database.database import db_base
from sqlalchemy import Column, Date, Time, Integer

class Luminosidade (db_base):
    __tablename__ = "temperatura"
    id   = Column(Integer, primary_key = True)
    data = Column(Date)
    hora = Column(Time)
    temperatura  = Column(Integer)

    def __init__(self, temperatura, data, hora):
        self.temperatura = temperatura
        self.data = data
        self.hora = hora
