from sqlalchemy import Column, Integer, String
from pokeapidata.models.basemodel import ModelBase


class PokemonMoves(ModelBase):
    __tablename__ = 'moves'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pokemon_name = Column('pokemon_name', String)
    move_name = Column('move_name', String)
    move_id = Column('move_id', String)
    level_learned_at = Column('level_learned_at', Integer)
    move_learn_method = Column('move_learn_method', String)
    version_group = Column('version_group', String)