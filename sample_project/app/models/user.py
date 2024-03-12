from sqlalchemy import (
    Integer,
    String,
)
from base import Base, TimeStampMixin
from sqlalchemy.orm import mapped_column, relationship


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    full_name = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), nullable=False, unique=True)
    password_hash = mapped_column(String(255), nullable=False)

    messages = relationship("Message", back_populates="user")
