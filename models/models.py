from sqlalchemy import Column, SmallInteger, VARCHAR, ForeignKey, TIMESTAMP
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'


    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))
