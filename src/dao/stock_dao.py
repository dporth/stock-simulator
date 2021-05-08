import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import db_session
from src.db.models import Stock

class StockDAO():

    def get_stocks(self):
        """Returns all stocks."""
        return db_session.query(Stock)

    def get_stock_by_symbol(self, symbol):
        """Returns all stocks that have the symbol provided."""
        return db_session.query(Stock).filter_by(symbol=symbol)

    def get_stock_by_id(self, stock_id):
        """Returns all stocks that have the stock id provided."""
        return db_session.query(Stock).filter_by(stock_id=stock_id)

    def delete_stock(self, symbol):
        """Deletes all records in the stock table that have the symbol specified. Returns the stock id of all records deleted."""
        marked_to_delete = []
        results = db_session.query(Stock.stock_id).filter_by(symbol=symbol)
        for row in results:
            marked_to_delete.append(row[0])
        stock = db_session.query(Stock).filter_by(symbol=symbol).delete()
        db_session.flush()
        return marked_to_delete

    def create_stock(self, symbol):
        """Creates a record in the stock table with the symbol specified. Returns the stock id of the new record."""
        stock = Stock(symbol=symbol)
        db_session.add(stock)
        db_session.flush()
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