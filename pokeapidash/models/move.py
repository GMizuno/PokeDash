from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import registry

from pokeapidash.models.basemodel import ModelBase

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class PokemonMoves(ModelBase):
    __table__ = Table(
        "moves",
        mapper_registry.metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('pokemon_name', String),
        Column('move_name', String),
        Column('move_id', String),
        Column('level_learned_at', Integer),
        Column('move_learn_method', String),
        Column('version_group', String)
    )

    pokemon_name: str
    move_name: str
    move_id: str
    level_learned_at: int
    move_learn_method: str
    version_group: str
