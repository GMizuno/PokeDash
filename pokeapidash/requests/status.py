import httpx
from dataclasses import dataclass

@dataclass
class PokeStatus:
    id: int
    poke_name: str
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

class Status:
    pass