from pokeapidash.session.db_session import insert_many
from pokeapidash.requests.moves import Moves
from pokeapidash.requests.pokemon import Pokemon

moves = Moves('https://pokeapi.co/api/v2/pokemon')
results = moves.extract
insert_many(results)


poke = Pokemon('https://pokeapi.co/api/v2/pokemon')
results = poke.extract
insert_many(results)