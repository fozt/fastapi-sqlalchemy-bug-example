from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import select

from src.tables import User, Role
from src.db import get_db, main

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await main()


@app.get("/get-user", response_model=Role)
async def root(
    db_session: AsyncSession = Depends(get_db),
):
    user = await db_session.execute(select(User))
    user = user.scalars().first()
    return user.role
