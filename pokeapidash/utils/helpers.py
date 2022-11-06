from pokeapidash.connector_db.connect import create_session
from pokeapidata.models.all_models import PokemonVersion, PokemonPokemon
from sqlalchemy import func


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


def get_status_by_type(pokemon: str):
    session = create_session()

    pokemon_type = session.query(PokemonPokemon.type_1, PokemonPokemon.type_2). \
        filter(PokemonPokemon.pokemon_name == pokemon).all()

    pokemon = session.query(
            func.avg(PokemonPokemon.hp).label('hp'),
            func.avg(PokemonPokemon.attack).label('attack'),
            func.avg(PokemonPokemon.defense).label('defense'),
            func.avg(PokemonPokemon.special_attack).label('special_attack'),
            func.avg(PokemonPokemon.special_defense).label('special_defense'),
            func.avg(PokemonPokemon.speed).label('speed'),
            func.avg(PokemonPokemon.height).label('height'),
            func.avg(PokemonPokemon.weight).label('weight')). \
        group_by(PokemonPokemon.type_1, PokemonPokemon.type_2). \
        filter(PokemonPokemon.type_1 == pokemon_type[0][0],
               PokemonPokemon.type_2 == pokemon_type[0][1]). \
        all()

    return pokemon

def get_data_for_radar(pokemon: str):
    return [get_status(pokemon), get_status_by_type(pokemon)]
