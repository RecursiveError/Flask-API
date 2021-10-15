from database.database import db_base
from sqlalchemy import Column, Date, Time, Integer

class Luminosidade (db_base):
    __tablename__ = "luminosidade"
    id   = Column(Integer, primary_key = True)
    data = Column(Date)
    hora = Column(Time)
    lux  = Column(Integer)

    def __init__(self, lux, data, hora):
        self.lux = lux
        self.data = data
        self.hora = hora


