from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL: str = 'postgresql://dvilkin:belhard@localhost:5432/bh33d'
DATABASE_ASYNC_URL: str = 'postgresql+asyncpg://dvilkin:belhard@localhost:5432/bh33d'
SYNC_ENGINE = create_engine(url=DATABASE_URL)
ASYNC_ENGINE = create_async_engine(DATABASE_ASYNC_URL)
Session = sessionmaker(bind=SYNC_ENGINE)


def create_sync_session(func):
    def wrapper(**kwargs):
        with Session as session:
            return func(**kwargs, session=session)

    return wrapper

def create_async_session(func):
    async def wrapper(**kwargs):
        async with AsyncSession(binds=ASYNC_ENGINE) as session:
            return await func(**kwargs, session=session)
    return wrapper
