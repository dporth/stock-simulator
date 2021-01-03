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
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address_id = Column(Integer, ForeignKey(f'{_db._schema}.address.address_id'))
    children = relationship("Account")

    def __repr__(self):
        return "<User(user_id='%s', first_name='%s', last_name='%s', address_id='%s')>" % (self.user_id, self.first_name, self.last_name, self.address_id)

class City(Base):
    __tablename__ = 'city'
    __table_args__ = {'schema' : _db._schema}
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    children = relationship("Address")

    def __repr__(self):
        return "<City(city_id='%s', city_name='%s')>" % (self.city_id, self.city_name)

class Country(Base):
    __tablename__ = 'country'
    __table_args__ = {'schema' : _db._schema}
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)
    children = relationship("Address")

    def __repr__(self):
        return "<Country(country_id='%s', country_name='%s')>" % (self.country_id, self.country_name)

class State(Base):
    __tablename__ = 'state'
    __table_args__ = {'schema' : _db._schema}
    state_id = Column(Integer, primary_key=True)
    state_name = Column(String)
    children = relationship("Address")
    
    def __repr__(self):
        return "<State(state_id='%s', state_name='%s')>" % (self.state_id, self.state_name)

class Address(Base):
    __tablename__ = 'address'
    __table_args__ = {'schema' : _db._schema}
    address_id = Column(Integer, primary_key=True)
    street = Column(String)
    postal_code = Column(String)
    state_id = Column(Integer, ForeignKey(f'{_db._schema}.state.state_id'))
    country_id = Column(Integer, ForeignKey(f'{_db._schema}.country.country_id'))
    city_id = Column(Integer, ForeignKey(f'{_db._schema}.city.city_id'))
    children = relationship("User")

    def __repr__(self):
        return "<Address(address_id='%s', street='%s', postal_code='%s', state_id='%s', country_id='%s', city_id='%s')>" % (self.address_id, self.street, self.postal_code, self.state_id, self.country_id, self.city_id)

class Account(Base):
    __tablename__ = 'account'
    __table_args__ = {'schema' : _db._schema}
    account_id = Column(Integer, primary_key=True)
    usd_amount = Column(Integer)
    share_amount = Column(Integer)
    stock_id = Column(Integer, ForeignKey(f'{_db._schema}.stock.stock_id'))
    user_id = Column(Integer, ForeignKey(f'{_db._schema}.user.user_id'))
    children = relationship("AccountValue")

    def __repr__(self):
        return "<Account(account_id='%s', usd_amount='%s', share_amount='%s', stock_id='%s', user_id='%s')>" % (self.account_id, self.usd_amount, self.share_amount, self.stock_id, self.user_id)

class AccountValue(Base):
    __tablename__ = 'account_value'
    __table_args__ = {'schema' : _db._schema}
    account_value_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey(f'{_db._schema}.account.account_id'))
    usd_account_amount = Column(Integer)
    valid_from = Column(DateTime, default=datetime.datetime.utcnow)
    valid_to = Column(DateTime)

    def __repr__(self):
        return "<AccountValue(account_value_id='%s', account_id='%s', valid_from='%s', valid_to='%s', usd_account_amount='%s')>" % (self.account_value_id, self.account_id, self.valid_from, self.valid_to, self.usd_account_amount)
