import sqlalchemy as sa
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.future.engine import Engine


def create_engine() -> Engine:
    conn_srt = "postgresql://postgres:092526@localhost:5432/pokedex"
    return sa.create_engine(url=conn_srt, echo=False)


def create_session() -> Session:
    engine = create_engine()
    session = sessionmaker(engine, expire_on_commit=False, class_=Session)

    return session()
