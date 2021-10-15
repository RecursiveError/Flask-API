from database.database import *
from models import luminosidade, temperatura

def init_db():
    db_base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()