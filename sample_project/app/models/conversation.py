from sqlalchemy import (
    Integer,
    insert,
)
from app.models.base import Base, TimeStampMixin
from sqlalchemy.orm import Session, mapped_column, relationship
from app.database.database import get_db_session


class Conversation(Base, TimeStampMixin):
    __tablename__ = "conversations"

    id = mapped_column(Integer, primary_key=True)
    messages = relationship("Message", back_populates="conversation")


def create_conversation(session: Session = None):

    def _execute_orm(session: Session):
        stmt = insert(Conversation).values()
        result = session.execute(stmt)
        return result.inserted_primary_key

    primary_key: int
    if session is None:
        with get_db_session() as session:
            primary_key: tuple = _execute_orm(session)
    else:
        primary_key: tuple = _execute_orm(session)

    return primary_key[0]
