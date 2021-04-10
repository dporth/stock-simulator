from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
import sys
[sys.path.append(i) for i in ['.', '..','../../']]
from .db_helper import DBHelper

Base = declarative_base()
_db = DBHelper()

class Stock(Base):
    __tablename__ = 'stock'
    __table_args__ = {'schema' : _db._schema}
    stock_id = Column(Integer, primary_key=True)
    symbol = Column(String)
    children = relationship("Account")
    children = relationship("StockPriceQueue")
    children = relationship("StockPriceHistory") 
    def __repr__(self):
        return "<Stock(stock_id='%s', symbol='%s')>" % (self.stock_id, self.symbol)

class StockPriceQueue(Base):
    __tablename__ = 'stock_price_queue'
    __table_args__ = {'schema' : _db._schema}
    queue_id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey(f'{_db._schema}.stock.stock_id'))
    etl_date = Column(String, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<StockPriceQueue(queue_id = '%s', stock_id='%s', etl_date='%s')>" % (self.queue_id, self.stock_id, self.etl_date)

class StockPriceHistory(Base):
    __tablename__ = 'stock_price_history'
    __table_args__ = {'schema' : _db._schema}
    stock_price_history_id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey(f'{_db._schema}.stock.stock_id'))
    historical_usd_price = Column(Integer)
    valid_from = Column(String, default=datetime.datetime.utcnow)
    valid_to = valid_to = Column(String)

    def __repr__(self):
        return "<StockPriceHistory(stock_price_history_id='%s', stock_id='%s', historical_used_price='%s', valid_from='%s', valid_to='%s')>" % (self.stock_price_history_id, self.stock_id, self.historical_usd_price, self.valid_from, self.valid_to)

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema' : _db._schema}
    user_id = Column(String, primary_key=True)
    identifier = Column(String)
    children = relationship("Account")

    def __repr__(self):
        return "<User(user_id='%s', identifier='%s')>" % (self.user_id, self.identifier)

class Account(Base):
    __tablename__ = 'account'
    __table_args__ = {'schema' : _db._schema}
    account_id = Column(Integer, primary_key=True)
    share_price = Column(Integer)
    share_amount = Column(Integer)
    stock_id = Column(Integer, ForeignKey(f'{_db._schema}.stock.stock_id'))
    user_id = Column(String, ForeignKey(f'{_db._schema}.user.user_id'))
    create_date = Column(String, default=datetime.datetime.utcnow)
    children = relationship("AccountValue")

    def __repr__(self):
        return "<Account(account_id='%s', share_price='%s', share_amount='%s', stock_id='%s', user_id='%s', create_date='%s')>" % (self.account_id, self.share_price, self.share_amount, self.stock_id, self.user_id, self.create_date)

class AccountValue(Base):
    __tablename__ = 'account_value'
    __table_args__ = {'schema' : _db._schema}
    account_value_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey(f'{_db._schema}.account.account_id'))
    usd_account_amount = Column(Integer)
    valid_from = Column(String, default=datetime.datetime.utcnow)
    valid_to = Column(String)
    children = relationship("AccountValueQueueUpdated")

    def __repr__(self):
        return "<AccountValue(account_value_id='%s', account_id='%s', valid_from='%s', valid_to='%s', usd_account_amount='%s')>" % (self.account_value_id, self.account_id, self.valid_from, self.valid_to, self.usd_account_amount)

class AccountValueQueueUpdated(Base):
    __tablename__ = 'account_value_queue_updated'
    __table_args__ = {'schema' : _db._schema}
    queue_updated_id = Column(Integer, primary_key=True)
    account_value_id = Column(Integer, ForeignKey(f'{_db._schema}.account_value.account_value_id'))
    etl_date = Column(String, default=datetime.datetime.utcnow)


    def __repr__(self):
        return "<AccountValue(queue_updated_id='%s', account_value_id='%s', etl_date='%s')>" % (self.queue_updated_id, self.account_value_id, self.etl_date)
