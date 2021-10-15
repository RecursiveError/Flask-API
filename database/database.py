from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://guilherme:anjos2020@localhost:5432/API-test')
db_session = scoped_session(sessionmaker(bind = engine))
db_base = declarative_base()
db_base.query = db_session.query_property()