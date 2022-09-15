from datetime import datetime

from sqlalchemy import Column, SmallInteger, VARCHAR, ForeignKey, TIMESTAMP, DECIMAL, CHAR, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    parent_id = Column(int, ForeignKey('categories.id', ondelete='CASCADE'))
    is_published = Column(Boolean, default=False, nullable=False)
    name = Column(VARCHAR(), nullable=False)

class Product(Base):
    __tablename__: str = 'products'

    id = Column(SmallInteger, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
    price = Column(DECIMAL(8, 2), nullable=False, default=0)
    media = Column(VARCHAR(20), nullable=False)
    total = Column(DECIMAL(8, 2), nullable=False, default=0)
    is_published = Column(Boolean, nullable=False, default=False)
    name = Column(VARCHAR(20), nullable=False)


class Status(Base):
    __tablename__: str = 'statuses'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)


class Languag(Base):
    __tablename__: str = 'languages'

    id = Column(SmallInteger, primary_key=True)
    language_code = Column(VARCHAR(20), nullable=False)


class