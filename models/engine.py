from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL: str = 'postgresql://dvilkin:helhard@localhost:5432/bh33d'
SYNC_ENGINE = create_engine(url=DATABASE_URL)
Session = sessionmaker(biod=SYNC_ENGINE)

def create_sync_session(func):
    def wrapper(**kwargs):
        with Session as session:
            return func(**kwargs, session=session)
    return wrapper
