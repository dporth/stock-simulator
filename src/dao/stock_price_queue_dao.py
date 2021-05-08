import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import db_session
from src.db.models import StockPriceQueue
from sqlalchemy import and_


class StockPriceQueueDAO():

    def add_stock_to_queue(self, stock_id):
        """Adds a stock to the queue with the given stock_id."""
        stock_price_queue = StockPriceQueue(stock_id=stock_id)
        db_session.add(stock_price_queue)
        db_session.commit()
        return stock_price_queue.queue_id

    def get_stock_from_queue(self, stock_id):
        """Returns query to get stock from queue with the given id."""
        return db_session.query(StockPriceQueue).filter_by(stock_id=stock_id)
    

    def pop_stock_queue(self):
        """Returns stock id and removes it from queue table."""
        result = db_session.query(StockPriceQueue).order_by(StockPriceQueue.etl_date.desc()).first()
        if result:
            stock_id = result.stock_id
            db_session.query(StockPriceQueue).filter_by(stock_id=stock_id).delete()
            return stock_id
        return None