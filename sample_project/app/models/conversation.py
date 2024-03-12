from sqlalchemy import (
    Integer,
)
from base import Base, TimeStampMixin
from sqlalchemy.orm import mapped_column, relationship


class Conversation(Base, TimeStampMixin):
    __tablename__ = "conversations"

    id = mapped_column(Integer, primary_key=True)
    messages = relationship("Message", back_populates="conversation")
