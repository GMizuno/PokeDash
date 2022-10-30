import sqlalchemy as sa
from pokeapidash.models.basemodel import ModelBase


class PokemonMoves(ModelBase):
    __tablename__ = 'moves'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    pokemon_name = sa.Column(sa.String)
    move_name = sa.Column(sa.String)
    move_id = sa.Column(sa.String)
    level_learned_at = sa.Column(sa.Integer)
    move_learn_method = sa.Column(sa.String)
    version_group = sa.Column(sa.String)
