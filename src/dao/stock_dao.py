import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Stock

class StockDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_stock(self):
        """Returns all stocks."""
        with self._db.session_scope() as session:
            return session.query(Stock)

    def delete_stock(self, symbol):
        """Deletes all records in the stock table that have the symbol specified."""
        with self._db.session_scope() as session:
            session.query(Stock).filter_by(symbol=symbol).delete()
            session.flush()

    # todo return stock id
    def create_stock(self, symbol):
        """Creates a record in the stock table with the symbol specified"""
        with self._db.session_scope() as session:
            stock = Stock(symbol=symbol)
            session.add(stock)
            session.flush()

if __name__ == "__main__":
    stock = StockDAO()
    # Insert stock functionality
    symbol = 'VOO'
    stock.create_stock(symbol)

    # Get stock functionality
    results = stock.get_stock()
    for row in results:
        print(row)

    # Delete stock funcitonality
    stock.delete_stock(symbol)