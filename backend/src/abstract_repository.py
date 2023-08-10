from abc import ABC, abstractmethod
from typing import Any, Sequence
from sqlalchemy import insert, select, ColumnElement

from database import sessionmaker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, filter):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, filter):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int | None:
        async with sessionmaker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one_or_none()

    async def get_one(self, filter: ColumnElement[bool]) -> Any | None:
        async with sessionmaker() as session:
            stmt = select(self.model).where(filter)
            result = await session.execute(stmt)
            return result.scalars().first()

    async def get_all(self, filter: ColumnElement[bool]) -> Sequence[Any]:
        async with sessionmaker() as session:
            stmt = select(self.model).where(filter)
            result = await session.execute(stmt)
            return result.scalars().all()
