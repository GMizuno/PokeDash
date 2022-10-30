from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import registry

from pokeapidash.models.basemodel import ModelBase

mapper_registry = registry()


@mapper_registry.mapped
@dataclass
class PokemonPokemon(ModelBase):
    __table__ = Table(
        "moves",
        mapper_registry.metadata,
        Column('id', Integer, primary_key=True),
        Column('pokemon_name', String),
        Column('hp', Integer),
        Column('attack', Integer),
        Column('defense', Integer),
        Column('special_attack', Integer),
        Column('special_defense', Integer),
        Column('speed', Integer),
        Column('height', Integer),
        Column('weight', Integer),
        Column('front_sprite', String),
        Column('back_sprite', String)
    )

    id: int
    pokemon_name: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    height: int
    weight: int
    front_sprite: str
    back_sprite: str
