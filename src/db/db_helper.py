import pyodbc
import sys
[sys.path.append(i) for i in ['.', '..','../../']]
from src.config import config

class DBHelper:
    
    __connection = None
    __cursor = None

    def __init__(self):
        __db_config = config['mssql']
        self.__connection = pyodbc.connect(f"driver=ODBC Driver 17 for SQL Server;server={__db_config['server']}; " \
                        f"database={__db_config['database']};uid={__db_config['user']};pwd={__db_config['password']}; " \
                        f"Trusted_Connection=yes;")
        self.__cursor = self.__connection.cursor()

    def query(self, query, params):
        if params:
            self.__cursor.execute(query, params)
        else:
            self.__cursor.execute(query)
        return self.__cursor

    def close(self):
        self.__connection.close()

db = DBHelper()
c = db.query('SELECT * FROM sys.tables;', '')
for row in c:
    print(row)
