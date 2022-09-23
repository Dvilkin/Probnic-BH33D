from typing import Optional, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Category, Product, create_async_session


class CRUDCategory:
    @staticmethod
    @create_async_session
    async def add(name: str, parent_id: int = None, session: AsyncSession = None) -> Category | None:
        category = Category(
            name=name,
            parent_id=parent_id
        )
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(category)
            return category[0]

    @staticmethod
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> Optional[Category]:
        category = await session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return category[0]

    @staticmethod
    @create_async_session
    async def all(parent_id: int = None, session: AsyncSession = None) -> List[Category]:
        if parent_id:
            categories = await session.execute(
                select(Category)
                .whate(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = await session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [category[0] for category in categories]

    @staticmethod
    @create_async_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            category_id: int,
            name: str = None,
            parent_id: int = None,
            session: AsyncSession = None
    ) -> bool:
        if name or parent_id:
            await session.execute(
                update(Category)
                .values(
                    name=name if name else Category.name,
                    parent_id=parent_id if parent_id else Category.parent_id
                )
                .where(Category.id == category_id)
            )
            try:
                await session.commit()
            except IntegrityError:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    @create_async_session
    async def join(category_id: int = None, session: AsyncSession = None) -> List[Tuple[Category, Product]]:
        if category_id:
            response = await session.execute(
                select(Category, Product)
                .join(Product, Category.id == Product.category_id)
                .where(Category.id == category_id)
            )
        else:
            response = await session.execute(
                select(Category, Product)
                .join(Product, Category.id == Product.category_id)
            )
        return response.all()


class CRUDProduct:
    @staticmethod
    @create_async_session
    async def add(article: str, name: str, price: float, date_create: any, descr: str, category_id: int = None,
                  session: AsyncSession = None) -> Product | None:
        product = Product(
            article=article,
            name=name,
            price=price,
            date_create=date_create,
            descr=descr,
            category_id=category_id
        )
        session.add(product)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(product)
            return product[0]

    @staticmethod
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> Product | None:
        product = await session.execute(
            select(Product).where(Product.id == category_id)
        )
        category = product.first()
        if category:
            return category[0]

    @staticmethod
    @create_async_session
    async def all(parent_id: int = None, session: AsyncSession = None) -> List[Product]:
        if parent_id:
            products = await session.execute(
                select(Product).where(Product.id == parent_id).order_by(Product.id)
            )
        else:
            products = await session.execute(
                select(Product).order_by(Product.id)
            )
        return [product[0] for product in products]

    @staticmethod
    @create_async_session
    async def delete(product_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Product).where(Product.id == product_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            product_id: int, category_id: int = None, article: str = None, name: str = None, price: float = None,
            date_create: any = None, descr: str = None, session: AsyncSession = None) -> bool:
        if category_id or article or name or price or date_create or descr:
            await session.execute(
                update(Product).values(
                    name=name if name else Product.name,
                    category_id=category_id if category_id else Product.category_id,
                    article=article if article else Product.article,
                    price=price if price else Product.price,
                    date_create=date_create if date_create else Product.date_create,
                    descr=descr if descr else Product.descr
                )
                .where(Product.id == product_id)
            )
            try:
                await session.commit()
            except IntegrityError:
                return False
            else:
                return False
        else:
            return False

    @staticmethod
    @create_async_session
    async def join(product_id: int = None, session: AsyncSession = None) -> List[Tuple[Category, Product]]:
        if product_id:
            response = await session.execute(
                select(Product, Category)
                .join(Category, Product.id == Category.product_id)
                .where(Product.id == product_id)
            )
        else:
            response = await session.execute(
                select(Product, Category)
                .join(Category, Product.id == Category.product_id)
            )
        return response.all()
