from sqlalchemy import (
    ForeignKey,
    Integer,
    Text,
    text,
)
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.dialects.mysql import TINYINT
from app.models.base import Base, TimeStampMixin


class Message(Base, TimeStampMixin):
    __tablename__ = "messages"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    conversation_id = mapped_column(
        ForeignKey("conversations.id"), nullable=False, index=True
    )
    message = mapped_column(Text, nullable=False)
    is_read = mapped_column(TINYINT(1), server_default=text("'0'"))

    conversation = relationship("Conversation", back_populates="messages")
    user = relationship("User", back_populates="messages")
