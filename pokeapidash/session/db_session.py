import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from pokeapidash.models.basemodel import ModelBase
import pokeapidash.models.all_models


def create_engine() -> Engine:
    conn_srt = "postgresql://postgres:092526@localhost:5432/pokedex"
    return sa.create_engine(url=conn_srt, echo=False)

def create_session() -> Session:
    engine = create_engine()
    session = sessionmaker(engine, expire_on_commit=False, class_=Session)

    return session()

def create_tables() -> None:
    engine = create_engine()
    ModelBase.metadata.drop_all(engine)
    ModelBase.metadata.create_all(engine)

