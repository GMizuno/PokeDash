from sqlalchemy import Column, Integer, String
from pokeapidata.models.basemodel import ModelBase


class PokemonPokemon(ModelBase):
    __tablename__ = 'pokemon'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pokemon_name = Column('pokemon_name', String)
    base_experience = Column('base_experience', Integer)
    hp = Column('hp', Integer)
    attack = Column('attack', Integer)
    defense = Column('defense', Integer)
    special_attack = Column('special_attack', Integer)
    special_defense = Column('special_defense', Integer)
    speed = Column('speed', Integer)
    type_1 =  Column('type_1', String)
    type_2 =  Column('type_2', String)
    height = Column('height', Integer)
    weight = Column('weight', Integer)
    front_sprite = Column('front_sprite', String)
    back_sprite = Column('back_sprite', String)
