from datetime import datetime

from sqlalchemy import Column, SmallInteger, VARCHAR, ForeignKey, TIMESTAMP, DECIMAL, CHAR, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, Primary_key=True)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    is_published = Column(Boolean, default=False, nullable=False)
    name = Column(VARCHAR(), nullable=False)

class Product(Base):
    __tablename__: str = 'products'

    id = Column(SmallInteger, Primary_key=True)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    price = Column(DECIMAL(8, 2), nullable=False, default=0)
    media = Column(VARCHAR(20), nullable=False)
    total = Column(DECIMAL(8, 2), nullable=False, default=0)
    is_published = Column(Boolean, nullable=False, default=False)
    name = Column(VARCHAR(20), nullable=False)


class Status(Base):
    __tablename__: str = 'statuses'

    id = Column(SmallInteger, Primary_key=True)
    name = Column(VARCHAR(20), nullable=False)


class Language(Base):
    __tablename__: str = 'languages'

    id = Column(SmallInteger, Primary_key=True)
    language_code = Column(VARCHAR(20), nullable=False)


class User(Base):
    _tablename__: str = 'users'

    id = Column(SmallInteger, Primary_key=True)
    is_blocked = Column(Boolean, nullable=False)
    balance = Column(DECIMAL(8, 2), nullable=False)
    language_id = Column(SmallInteger, ForeignKey('languages.id', ondelete='NO ACTION'), nullable=False)


class Invoice(Base):
    __tablename__: str = 'invoices'

    id = Column(SmallInteger, Primary_key=True)
    user_id = Column(SmallInteger, ForeignKey('users.id', ondelete='NO ACTIONS'), nullable=False)
    data_create = Column(TIMESTAMP, default=datetime.utcnow())
    total = Column(DECIMAL(8, 2), nullable=False)
    status_id = Column(SmallInteger, ForeignKey('statuses.id', ondelete='NO ACTION'), nullable=False)


class Order(Base):
    __tablename__: str = 'orders'

    id = Column(SmallInteger, Primary_key=True)
    user_id = Column(SmallInteger, primary_key=False)
    date_create = Column(TIMESTAMP, default=datetime.utcnow())
    status_id = Column(SmallInteger, ForeignKey('statuses.id', ondelete='NO ACTION'), nullable=False)
    invoice_id = Column(ForeignKey('invoices.id', ondelete='NO ACTIONS'), nullable=False)4


class Order_item(Base):
    __tablename__: str = 'order_items'

    id = Column(SmallInteger, Primary_key=True)
    order_id = Column(SmallInteger, ForeignKey('order_items.id', ondelete='NO ACTION'), nullable=False)
    product_id = Column(SmallInteger, ForeignKey('products.id', ondelete='NO ACTION'), nullable=False)
    total = Column(DECIMAL(8,2), nullable=False)
