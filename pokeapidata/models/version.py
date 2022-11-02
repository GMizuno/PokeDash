from sqlalchemy import Column, Integer, String
from pokeapidata.models.basemodel import ModelBase

class PokemonVersion(ModelBase):
    __tablename__ = 'version'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    pokemon_name = Column('pokemon_name', String)
    generation = Column('generation', String)
    region = Column('region', String)