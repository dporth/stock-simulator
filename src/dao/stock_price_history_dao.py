import sys
[sys.path.append(i) for i in ['.', '..','../../', '../db/']]
from src.db.db_helper import DBHelper
from src.db.models import StockPriceHistory
from sqlalchemy import and_


class StockPriceHistoryDAO():

    def __init__(self):
        self._db = DBHelper()

    def get_stock_value(self, stock_id):
        """Returns the latest value for the given stock id."""
        with self._db.session_scope() as session:
            return session.query(StockPriceHistory).filter(and_(StockPriceHistory.stock_id==stock_id, StockPriceHistory.valid_to == None))
    


            