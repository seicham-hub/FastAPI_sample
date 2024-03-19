from sqlalchemy import (
    Integer,
    String,
    select,
)
from app.models.base import Base, TimeStampMixin
from sqlalchemy.orm import mapped_column, relationship
from app.database.database import Session
from typing import Optional


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    full_name = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), nullable=False, unique=True)
    password_hash = mapped_column(String(255), nullable=False)

    messages = relationship("Message", back_populates="user")


def get_user_by_id(user_id: int) -> Optional[User]:
    with Session() as session:
        stmt = select(User).where(User.id == user_id)
        result = session.execute(stmt).first()

    return result


def get_user_by_email(email: str) -> Optional[User]:
    with Session() as session:
        stmt = select(User).where(User.email == email)
        result = session.scalar(stmt)

    return result


def get_all_user() -> list[User]:

    with Session() as session:
        stmt = select(User)
        result = session.scalars(stmt).all()

    return result
