from sqlalchemy import (
    Integer,
    ForeignKey,
    insert,
)
from app.models.base import Base, TimeStampMixin
from sqlalchemy.orm import Session, mapped_column
from app.database.database import get_db_session


class ConversationUserRelation(Base, TimeStampMixin):
    __tablename__ = "conversation_user_relation"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    conversation_id = mapped_column(
        ForeignKey("conversations.id"), nullable=False, index=True
    )


def create_conversation_user_relation(values: list[dict], session: Session = None):

    def _execute_orm(session: Session):
        stmt = insert(ConversationUserRelation)
        session.execute(stmt, values)

    if session is None:
        with get_db_session() as session:
            _execute_orm(session)
    else:
        _execute_orm(session)
