import httpx
from dataclasses import dataclass

@dataclass
class PokePokemon:
    poke_id: int
    poke_name: str
    heigt: int
    weigth: int
    front_sprite: str
    back_sprite: str
    base_xp: int

r = httpx.get('https://pokeapi.co/api/v2/pokemon/2/').json()

class Pokemon:
    pass
