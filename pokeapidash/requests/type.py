import httpx
from dataclasses import dataclass

@dataclass
class PokeType:
    id: int
    poke_name: str
    type1: str
    type2: str

class Type:
    pass