# document:https://docs.sqlalchemy.org/en/20/orm/declarative_mixins.html

from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declared_attr


class Base(DeclarativeBase):
    pass


class TimeStampMixin(object):
    @declared_attr
    def created_at(cls):
        return mapped_column(DateTime, server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return mapped_column(
            DateTime,
            server_default=func.now(),
            onupdate=func.now(),
        )

    @declared_attr
    def deleted_at(cls):
        return mapped_column(DateTime)
