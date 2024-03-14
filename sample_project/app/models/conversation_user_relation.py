from sqlalchemy import (
    Integer,
    ForeignKey,
)
from app.models.base import Base, TimeStampMixin
from sqlalchemy.orm import mapped_column


class ConversationUserRelation(Base, TimeStampMixin):
    __tablename__ = "conversation_user_relation"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    conversation_id = mapped_column(
        ForeignKey("conversations.id"), nullable=False, index=True
    )
