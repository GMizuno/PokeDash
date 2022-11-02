import sqlalchemy as sa
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.future.engine import Engine

from pokeapidata.models.basemodel import ModelBase
import pokeapidata.models.all_models


def create_engine() -> Engine:
    conn_srt = "postgresql://postgres:092526@localhost:5432/pokedex"
    return sa.create_engine(url=conn_srt, echo=False)

def create_session() -> Session:
    engine = create_engine()
    session = sessionmaker(engine, expire_on_commit=False, class_=Session)

    return session()

def create_tables() -> None:
    engine = create_engine()
    print(ModelBase.metadata)
    ModelBase.metadata.drop_all(engine)
    ModelBase.metadata.create_all(engine)

def insert_one(data):
    with create_session() as session:
        session.add(data)
        session.commit()

def insert_many(data):
    with create_session() as session:
        session.add_all(data)
        session.commit()

