import pyodbc
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import sys
[sys.path.append(i) for i in ['.', '..','../../']]
from src.config import config

class DBHelper(object):

    def __init__(self):
        _db_config = config['mssql']
        self._schema = _db_config['schema']
        self._engine = sa.create_engine(f"mssql+pyodbc://{_db_config['user']}:{_db_config['password']}@{_db_config['server']}/{_db_config['database']}?driver=ODBC Driver 17 for SQL Server?Trusted_Connection=yes’")
        self._session = sessionmaker(bind=self._engine)
        #Base.metadata.drop_all(bind=self._engine)
        #Base.metadata.create_all(bind=self._engine)

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
