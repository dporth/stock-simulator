import sys
[sys.path.append(i) for i in ['.', '..','../../']]
import requests
import json
from decimal import Decimal
from src.config import polygon_queue_api_key, polygon_stock_eod_endpoint
from src.dao.stock_price_queue_dao import StockPriceQueueDAO
from src.dao.stock_price_history_dao import StockPriceHistoryDAO
from src.dao.stock_dao import StockDAO
from src.dao.account_dao import AccountDAO
from src.dao.account_value_dao import AccountValueDAO



class LoadQueueStockPrices():
    def __init__(self):
        self._queue = StockPriceQueueDAO()
        self._stock = StockDAO()
        self._stock_history = StockPriceHistoryDAO()
        self._account = AccountDAO()
        self._account_value = AccountValueDAO()

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
        """Sends a request to stock market api to retrieve the latest prices for the stock."""
        return requests.get(polygon_stock_eod_endpoint.format(ticker=symbol, key=polygon_queue_api_key))

    def update_stock_account_values(self, stock_id, eod_value):
        """Creates a stock account value for each stock account that is for the specified stock_id."""
        # Create stock account values for stocks that just were popped from queue
        account_ids = []
        result = self._account.get_accounts_by_stock(stock_id)
        for row in result:
            account = {"account_id": row.account_id, "usd_account_amount":row.share_amount* Decimal(eod_value)}
            account_ids.append(account)
        for each in account_ids:
            self._account_value.expire_account_value(each["account_id"], each["usd_account_amount"])

if __name__ == '__main__':
    etl = LoadQueueStockPrices()
    for i in range(1,6):
        stock_id = etl.pop_stock_queue()
        if stock_id:
            symbol = etl.get_stock_symbol(stock_id)
            response = etl.request_eod_stock_values(symbol)
            eod_value = json.loads(response.text)['results'][0]['c']
            etl.update_stock_price_history(symbol, eod_value)
            etl.update_stock_account_values(stock_id, eod_value)






