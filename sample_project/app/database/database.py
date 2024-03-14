from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from contextlib import contextmanager

DATABASE_URL = URL.create(
    "mysql+pymysql",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    database=os.environ["DB_NAME"],
)

engine = create_engine(
    DATABASE_URL,
    echo="debug",
    # core*2の値が良い
    pool_size=5,
    pool_recycle=3600,
)

# session_makerのみ使用して一つのインスタンスを使いまわすと、スレッドセーフでない
# scoped_sessionは何度インスタンス化しても一つのセッションを使う
# マルチスレッドの場合は新規インスタンスが作成される
Session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
)


@contextmanager
def get_db_session():
    try:
        session = Session()
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
