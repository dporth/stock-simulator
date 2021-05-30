import pyodbc
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from contextlib import contextmanager
import sys
[sys.path.append(i) for i in ['.', '..','../../']]
from src.config import config
from sqlalchemy.ext.declarative import declarative_base

_db_config = config['mssql']
schema = _db_config['schema']
engine = sa.create_engine(f"mssql+pyodbc://{_db_config['user']}:{_db_config['password']}@{_db_config['server']}/{_db_config['database']}?driver=ODBC+Driver+17+for+SQL+Server")
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import src.db.models
    Base.metadata.create_all(bind=engine)

@contextmanager
def session_scope(self):
    """Provide a transactional scope around a series of operations."""
    session = self._session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == "__main__":
    db = DBHelper()
    with db.session_scope() as session:
        result = session.execute("select * from sys.tables;")
        for row in result:
            print(row)
