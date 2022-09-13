from datetime import datetime

from sqlalchemy import Column, SmallInteger, VARCHAR, ForeignKey, TIMESTAMP, DECIMAL
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'


    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))


class Product(Base):
    __tablenam__: str = 'products'

    article = Column(CHAR(), primary_key=True)
    name = Column(VARCHAR(), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False, default=0)
    date_create = Column(TIMESTAMP, default=datatime.utcnow())
    descr = Column(VARCHAR(140))


class User(Base):
    __tablename__: str = 'users'

    id = Column(CHAR(), primary_key=True)
    name = Column(VARCHAR(36), nullable=False)
    email = Column(VARCHAR(36), nullable=False, unique=True)


class Order(Base):
    _tablename__: str = 'orders'

    id = Column(SmallInteger, primary_key=True)
    user_id = Column(SmallInteger, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    is_paid = Column(Boolean, default=False, nullable=False)
    data_create = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False)


class OrderItem(Base):
    _tablename__: str = 'orders_items'

    id = Column(SmallInteger, Primary_key=True)
    product_article = Column(Char(6), ForeignKey('products.article', ondelete='NOACTION'), nullable=False)
    order_id = Column(ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
