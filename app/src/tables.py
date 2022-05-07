from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    role_id: Optional[int] = Field(nullable=False, foreign_key="role.id")
    role: Optional["Role"] = Relationship(
        back_populates="users", sa_relationship_kwargs={"lazy": "selectin"}
    )


class Role(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    users: List["User"] = Relationship(
        back_populates="role", sa_relationship_kwargs={"lazy": "selectin"}
    )
