from pokeapidash.connector_db.connect import create_session
from pokeapidata.models.all_models import PokemonMoves, PokemonVersion, PokemonPokemon
from sqlalchemy import func
from sqlalchemy.orm import Session


def get_generation():
    session = create_session()

    gen = session.query(PokemonVersion.generation, func.min(PokemonVersion.id)).group_by(PokemonVersion.generation).all()

    return [i[0] for i in sorted(gen, key=lambda tup: tup[1])] + ['all']

def get_region():
    session = create_session()

    gen = session.query(PokemonVersion.region, func.min(PokemonVersion.id)).group_by(PokemonVersion.region).all()

    return [i[0] for i in sorted(gen, key=lambda tup: tup[1])] + ['all']
