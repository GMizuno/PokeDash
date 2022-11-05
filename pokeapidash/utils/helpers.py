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


def get_status(pokemon: str):
    session = create_session()

    pokemon = session.query(PokemonPokemon.hp,
                            PokemonPokemon.attack,
                            PokemonPokemon.defense,
                            PokemonPokemon.special_attack,
                            PokemonPokemon.special_defense,
                            PokemonPokemon.speed,
                            PokemonPokemon.height,
                            PokemonPokemon.weight). \
        filter(PokemonPokemon.pokemon_name == pokemon).all()

    return pokemon


def get_front_img(pokemon: str):
    session = create_session()

    pokemon = session.query(PokemonPokemon.front_sprite). \
        filter(PokemonPokemon.pokemon_name == pokemon).all()

    return pokemon[0][0]


def get_back_img(pokemon: str):
    session = create_session()

    pokemon = session.query(PokemonPokemon.back_sprite). \
        filter(PokemonPokemon.pokemon_name == pokemon).all()

    return pokemon[0][0]

get_front_img('muk')