from typing import Optional, List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from models import Category, Product, User, Order, OrderItem, create_async_session


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
                .where(Category.parent_id == parent_id)
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
    async def get(product_id: int, session: AsyncSession = None) -> Product | None:
        product = await session.execute(
            select(Product).where(Product.id == product_id)
        )
        category = product.first()
        if category:
            return category[0]

    @staticmethod
    @create_async_session
    async def all(product_id: int = None, session: AsyncSession = None) -> List[Product]:
        if product_id:
            products = await session.execute(
                select(Product).where(Product.id == product_id).order_by(Product.id)
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


class CRUDUser:
    @staticmethod
    @create_async_session
    async def add(name: str, email: str, session: AsyncSession = None) -> User | None:
        user = User(
            name=name,
            email=email
        )
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(user)
            return user[0]

    @staticmethod
    @create_async_session
    async def get(user_id: int, session: AsyncSession = None) -> User | None:
        user = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = user.first()
        if user:
            return user[0]

    @staticmethod
    @create_async_session
    async def all(user_id: int = None, session: AsyncSession = None) -> List[User]:
        if user_id:
            users = await session.execute(
                select(User)
                .where(User.user_id == user_id)
                .order_by(User.id)
            )
        else:
            users = await session.execute(
                select(User)
                .order_by(User.id)
            )
        return [user[0] for user in users]

    @staticmethod
    @create_async_session
    async def delete(user_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(user_id: int, name: str = None, email: str = None, session: AsyncSession = None) -> bool:
        if name or email:
            await session.execute(
                update(User)
                .values(
                    name=name if name else User.name,
                    email=email if email else User.email
                )
                .where(User.id == user_id)
            )
            try:
                await session.commit()
            except IntegrityError:
                return False
            else:
                return True
        else:
            return False


class CRUDOrder:
    @staticmethod
    @create_async_session
    async def add(user_id: int, is_paid: bool = None, data_create: any = None, session: AsyncSession = None
                  ) -> Order | None:
        order = Order(
            user_id=user_id,
            is_paid=is_paid,
            data_create=data_create
        )
        session.add(order)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(order)
            return order[0]

    @staticmethod
    @create_async_session
    async def get(order_id: int, session: AsyncSession = None) -> Order | None:
        order = await session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return order[0]

    @staticmethod
    @create_async_session
    async def all(user_id: int = None, session: AsyncSession = None) -> List[Order]:
        if user_id:
            orders = await session.execute(
                select(Order)
                .where(Order.user_id == user_id)
                .order_by(Order.id)
            )
        else:
            orders = await session.execute(
                select(Order)
                .order_by(Order.id)
            )
        return [order[0] for order in orders]

    @staticmethod
    @create_async_session
    async def delete(order_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Order)
            .where(Order.id == order_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            order_id: int,
            user_id: int,
            is_paid: bool,
            data_create: any,
            session: AsyncSession = None
    ) -> Order | None:
        order = Order(
            order_id=order_id,
            user_id=user_id,
            is_paid=is_paid,
            data_create=data_create
        )
        session.add(order)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(order)
            return order[0]

    @staticmethod
    @create_async_session
    async def join(order_id: int = None, session: AsyncSession = None) -> List[Tuple[Order, User]]:
        if order_id:
            response = await session.execute(
                select(Order, User)
                .join(User, Order.id == User.order_id)
                .where(Order.id == order_id)
            )
        else:
            response = await session.execute(
                select(Order, User)
                .join(User, Order.id == User.order_id)
            )
        return response.all()


class CRUDOrderItem:
    @staticmethod
    @create_async_session
    async def add(product_article: int = None, order_id: int = None, session: AsyncSession = None) -> OrderItem | None:
        orderitem = OrderItem(
            product_article=product_article,
            order_id=order_id
        )
        session.add(orderitem)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(orderitem)
            return orderitem[0]

    @staticmethod
    @create_async_session
    async def get(orderitem_id: int, session: AsyncSession = None) -> OrderItem | None:
        orderitem = await session.execute(
            select(OrderItem).where(OrderItem.id == orderitem_id)
        )
        orderitem = orderitem.first()
        if orderitem:
            return orderitem[0]

    @staticmethod
    @create_async_session
    async def all(product_article: int = None, session: AsyncSession = None) -> List[OrderItem]:
        if product_article:
            orderitems = await session.execute(
                select(OrderItem)
                .where(OrderItem.product_article == product_article)
                .order_by(OrderItem.id)
            )
        else:
            orderitems = await session.execute(
                select(OrderItem)
                .order_by(OrderItem.id)
            )
        return [orderitem[0] for orderitem in orderitems]

    @staticmethod
    @create_async_session
    async def delete(orderitem_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(OrderItem)
            .where(OrderItem.id == orderitem_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            orderitem_id: int,
            product_article: int = None,
            order_id: int = None,
            session: AsyncSession = None
    ) -> bool:
        if product_article or order_id:
            await session.execute(
                update(OrderItem)
                .values(
                    product_article=product_article if product_article else OrderItem.product_article,
                    order_id=order_id if order_id else OrderItem.order_id,
                )
                .where(OrderItem.id == orderitem_id)
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
    async def join(orderitem_id: int = None, session: AsyncSession = None) -> List[Tuple[OrderItem, Order]]:
        if orderitem_id:
            response = await session.execute(
                select(OrderItem, Order)
                .join(Order, OrderItem.id == Order.orderitem_id)
                .where(OrderItem.id == orderitem_id)
            )
        else:
            response = await session.execute(
                select(OrderItem, Order)
                .join(Order, OrderItem.id == Order.orderitem_id)
            )
        return response.all()
