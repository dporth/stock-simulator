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
        """Returns query to get stock from queue with the given id."""
        with self._db.session_scope() as session:
            return session.query(StockPriceQueue).filter_by(stock_id=stock_id)
    

    def pop_stock_queue(self):
        """Returns stock id and removes it from queue table."""
        with self._db.session_scope() as session:
            result = session.query(StockPriceQueue).order_by(StockPriceQueue.etl_date.desc()).first()
            if result:
                stock_id = result.stock_id
                session.query(StockPriceQueue).filter_by(stock_id=stock_id).delete()
                return stock_id
        return None