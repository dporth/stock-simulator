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

    def __repr__(self):
        return "<Stock(stock_id='%s', symbol='%s')>" % (self.stock_id, self.symbol)

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema' : _db._schema}
    user_id = Column(String, primary_key=True)
    email = Column(String)
    children = relationship("Account")

    def __repr__(self):
        return "<User(user_id='%s', email='%s')>" % (self.user_id, self.email)

class Account(Base):
    __tablename__ = 'account'
    __table_args__ = {'schema' : _db._schema}
    account_id = Column(Integer, primary_key=True)
    usd_amount = Column(Integer)
    share_amount = Column(Integer)
    stock_id = Column(Integer, ForeignKey(f'{_db._schema}.stock.stock_id'))
    user_id = Column(String, ForeignKey(f'{_db._schema}.user.user_id'))
    children = relationship("AccountValue")

    def __repr__(self):
        return "<Account(account_id='%s', usd_amount='%s', share_amount='%s', stock_id='%s', user_id='%s')>" % (self.account_id, self.usd_amount, self.share_amount, self.stock_id, self.user_id)

class AccountValue(Base):
    __tablename__ = 'account_value'
    __table_args__ = {'schema' : _db._schema}
    account_value_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey(f'{_db._schema}.account.account_id'))
    usd_account_amount = Column(Integer)
    valid_from = Column(String, default=datetime.datetime.utcnow)
    valid_to = Column(String)

    def __repr__(self):
        return "<AccountValue(account_value_id='%s', account_id='%s', valid_from='%s', valid_to='%s', usd_account_amount='%s')>" % (self.account_value_id, self.account_id, self.valid_from, self.valid_to, self.usd_account_amount)
