from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
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

    def __repr__(self):
        return "<Stock(stock_id='%s', symbol='%s')>" % (self.stock_id, self.symbol)

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema' : _db._schema}
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    #implement
    #address_id = Column(Integer, ForeignKey('parent.id'))

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s')>" % (self.first_name, self.last_name)
