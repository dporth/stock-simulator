import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import Stock

class StockDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_stocks(self):
        """Returns all stocks."""
        with self._db.session_scope() as session:
            return session.query(Stock)

    def get_stock_by_symbol(self, symbol):
        """Returns all stocks that have the symbol provided."""
        with self._db.session_scope() as session:
            return session.query(Stock).filter_by(symbol=symbol)

    def delete_stock(self, symbol):
        """Deletes all records in the stock table that have the symbol specified. Returns the stock id of all records deleted."""
        with self._db.session_scope() as session:
            marked_to_delete = []
            results = session.query(Stock.stock_id).filter_by(symbol=symbol)
            for row in results:
                marked_to_delete.append(row[0])
            stock = session.query(Stock).filter_by(symbol=symbol).delete()
            session.flush()
            return marked_to_delete

    # todo return stock id
    def create_stock(self, symbol):
        """Creates a record in the stock table with the symbol specified. Returns the stock id of the new record."""
        with self._db.session_scope() as session:
            stock = Stock(symbol=symbol)
            session.add(stock)
            session.flush()
            return stock.stock_id

if __name__ == "__main__":
    stock = StockDAO()
    # Insert stock functionality
    symbol = 'VOO'
    print(stock.create_stocks(symbol))

    # Get stock functionality
    results = stock.get_stock()
    for row in results:
        print(row)

    # Delete stock funcitonality
    print(stock.delete_stock(symbol))