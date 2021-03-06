import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import StockPriceQueue
from sqlalchemy import and_


class StockPriceQueueDAO():

    def __init__(self):
        self._db = DBHelper()

    def add_stock_to_queue(self, stock_id):
        """Adds a stock to the queue with the given stock_id."""
        with self._db.session_scope() as session:
            stock_price_queue = StockPriceQueue(stock_id=stock_id)
            session.add(stock_price_queue)
            session.commit()
            return stock_price_queue.queue_id

    def get_stock_from_queue(self, stock_id):
        """Returns the queue result if the stock is in the queue."""
        with self._db.session_scope() as session:
            return session.query(StockPriceQueue).filter_by(stock_id=stock_id)
    

            