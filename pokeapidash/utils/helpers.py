from pokeapidash.connector_db.connect import create_session, create_engine
from pokeapidata.models.all_models import PokemonMoves, PokemonVersion, PokemonPokemon
from sqlalchemy import func
from sqlalchemy.orm import Session
import pandas as pd


def get_generation():
    session = create_session()

    gen = session.query(PokemonVersion.generation, func.min(PokemonVersion.id)).group_by(
            PokemonVersion.generation).all()

    return [i[0] for i in sorted(gen, key=lambda tup:tup[1])] + ['all']


def get_region():
    session = create_session()

    reg = session.query(PokemonVersion.region, func.min(PokemonVersion.id)).group_by(PokemonVersion.region).all()

    return [i[0] for i in sorted(reg, key=lambda tup:tup[1])] + ['all']


def get_pokemon_by_region(region: str = 'kanto'):
    session = create_session()

    if region != 'all':
        pokemon = session.query(PokemonPokemon.pokemon_name). \
            join(PokemonVersion, PokemonVersion.pokemon_name == PokemonPokemon.pokemon_name). \
            filter(PokemonVersion.region == region).all()

        return [i[0] for i in pokemon]

    pokemon = session.query(PokemonPokemon.pokemon_name)
    return [i[0] for i in pokemon]


get_pokemon_by_region()