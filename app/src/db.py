import asyncio
import logging
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from src.settings import settings
from src.tables import User, Role

engine = create_async_engine(
    settings.ASYNC_DATABASE_URI, echo=True, future=True, max_overflow=64
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


async def create_init_data():
    async with SessionLocal() as session:
        await init_db(session)


async def init_db(db_session: AsyncSession):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async def create_role(name: str) -> Role:
        db_obj = Role(name=name)
        db_session.add(db_obj)
        await db_session.commit()
        await db_session.refresh(db_obj)
        return db_obj

    async def create_user(name: str, role_id: int) -> User:
        db_obj = User(name=name, role_id=role_id)
        db_session.add(db_obj)
        await db_session.commit()
        await db_session.refresh(db_obj)
        return db_obj

    role = await create_role("role_1")
    await create_user(name="user_1", role_id=role.id)


async def main():
    logging.info("Creating initial data")
    await create_init_data()
    logging.info("Initial data created")


if __name__ == "__main__":
    asyncio.run(main())
