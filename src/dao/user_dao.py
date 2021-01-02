from src.db.DbHelper import DbHelper

class UserDAO(object):
   __db = None

   def __init__(self):
       self.__db = DbHelper()

   def getUsers(self):
       """Returns all users associated with the stock market simulator."""
       return self.__db.query("SELECT * FROM users", None).fetchall()