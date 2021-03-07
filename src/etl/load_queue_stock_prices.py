import sys
[sys.path.append(i) for i in ['.', '..','../']]
import requests
from time import strftime
import json
import pandas as pd
from decimal import Decimal
from src.config import polygon_queue_api_key, polygon_stock_eod_endpoint
from src.dao.stock_price_queue_dao import StockPriceQueueDAO
from src.dao.stock_price_history_dao import StockPriceHistoryDAO
from src.dao.stock_dao import StockDAO

class LoadQueueStockPrices():
    def __init__(self):
        self._queue = StockPriceQueueDAO()
        self._stock = StockDAO()
        self._stock_history = StockPriceHistoryDAO()

    def pop_stock_queue(self):
        """Pops the next item in the queue and returns its id."""
        stock_id = self._queue.pop_stock_queue()
        return stock_id

    def get_stock_symbol(self, stock_id):
        """Gets symbol from stock id."""
        result = self._stock.get_stock_by_id(stock_id).first()
        if result:
            symbol = result.symbol
        return symbol

    def update_stock_price_history(self, symbol, value):
        """Takes in a symbol and value and updates the historical usd account value in stock price history table."""
        return self._stock_history.create_stock_value(stock_id, value)

    def request_eod_stock_values(self, symbol):
        return requests.get(polygon_stock_eod_endpoint.format(ticker=symbol, key=polygon_queue_api_key))

if __name__ == '__main__':
    etl = LoadQueueStockPrices()
    for i in range(1,6):
        stock_id = etl.pop_stock_queue()
        if stock_id:
            symbol = etl.get_stock_symbol(stock_id)
            response = etl.request_eod_stock_values(symbol)
            eod_value = json.loads(response.text)['results'][0]['c']
            etl.update_stock_price_history(symbol, eod_value)





