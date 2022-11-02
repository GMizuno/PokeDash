from pokeapidata.requests.version import Version
from pokeapidata.session.db_session import insert_many
from pokeapidata.requests.moves import Moves
from pokeapidata.requests.pokemon import Pokemon

moves = Moves('https://pokeapi.co/api/v2/pokemon')
results = moves.extract
insert_many(results)


poke = Pokemon('https://pokeapi.co/api/v2/pokemon')
results = poke.extract
insert_many(results)

ulrs = ['https://pokeapi.co/api/v2/generation/1', 'https://pokeapi.co/api/v2/generation/2',
        'https://pokeapi.co/api/v2/generation/3', 'https://pokeapi.co/api/v2/generation/4',
        'https://pokeapi.co/api/v2/generation/5', 'https://pokeapi.co/api/v2/generation/6',
        'https://pokeapi.co/api/v2/generation/7', 'https://pokeapi.co/api/v2/generation/8']
version = Version(urls=ulrs)
results = version.extract
insert_many(results)
