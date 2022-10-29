import httpx
from dataclasses import dataclass


@dataclass
class PokeMoves:
    poke_name: str
    move_name: str
    move_id: str
    level_learned_at: int
    move_learn_method: str
    version_group: str

params = {'limit': '100000', 'offset': 0}
r = httpx.get('https://pokeapi.co/api/v2/pokemon', params=params)
results = r.json().get('results')
#
# r = httpx.get('https://pokeapi.co/api/v2/pokemon/2/').json()

class Moves:

    def __init__(self, url):
        self.url = url
        self.params = {'limit': '100000', 'offset': 0}

    def get_move_info(self, result: dict) -> list:
        moves = []
        poke_name = result.get('name')
        for x in result.get('moves'):
            move_name = x.get('move').get('name')
            url = x.get('move').get('url')
            for i in x.get('version_group_details'):
                level_learned_at = i.get('level_learned_at')
                move_learn_method = i.get('move_learn_method').get('name')
                version_group = i.get('version_group').get('name')
                moves.append(PokeMoves(poke_name, move_name, url, level_learned_at, move_learn_method, version_group))
        return moves

    def get_moves(self, url: str) -> list:
        p1 = httpx.get(url).json()
        return self.get_move_info(p1)

    @property
    def extract(self) -> list:
        print(self.url)
        urls = httpx.get(self.url, params=self.params).json().get('results')
        return [self.get_moves(url.get('url')) for url in urls]

m = Moves('https://pokeapi.co/api/v2/pokemon')
dados = m.extract