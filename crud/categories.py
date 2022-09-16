from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Category, create_sync_session


class CRUDCategory:
    @staticmethod
    @create_sync_session
    def __add__(name: str, parent_id: int = None, session: Session = None) -> Optional[Category]:
        category = Category(
            name=name,
            parent_id=parent_id
        )
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(category)
            return category[0]


@staticmethod
@create_sync_session
def get(category_id: int, session: Session = None) -> Optional[Category]:
    catrgory = session.execute(
        select(Category).where(Category.id == category_id)
    )
    response = catrgory.first()
    if response:
        return response[0]

@staticmethod
@create_sync_session
def all(parent_id: int = None, session: Session = None) -> List[Category]:
    if parent_id:
        categories = session.execute(
            select(Category)
            .whate(Category.parent_id == parent_id)
            .order_by(Category.id)
        )
    else:
        categories = session.execute(
        select(Category)
        .order_by(Category.id)
        )
    return [category[0] for category in categories]

@staticmethod
@create_sync_session
def delete(category_id: int, session: Session = None) -> None:
    session.execute(
        delete(Category)
        .where(Category.id = category_id)
    )
    session.commit()

@staticmethod
@create_sync_session
def update(
        category_id: int,
        name: str = None,
        parent_id: int = None,
        session: Session = None
) -> bool:
    if name or parent_id:
        session.execute(
            update(Category)
            .values(
                name=name if name else Category.name,
                parent_id=parent_id if parent_id else Category.parent_id
            )
            .where(Category.id == category_id)
        )
        try:
            session.commit()
        except IntegrityError:
            return  False
        else:
            return True
    else:
        return False
