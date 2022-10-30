import httpx
from dataclasses import dataclass
from pokeapidash.session.db_session import create_session
from pokeapidash.models.move import PokemonMoves


@dataclass
class PokeMoves:
    poke_name: str
    move_name: str
    move_id: str
    level_learned_at: int
    move_learn_method: str
    version_group: str


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
        print(url)
        return self.get_move_info(p1)

    @property
    def extract(self) -> list:
        urls = httpx.get(self.url, params=self.params).json().get('results')
        return [self.get_moves(url.get('url')) for url in urls]

    def insert_table(self):
        moves = self.extract
        session = create_session()
        session.add_all(moves)
        session.commit()


moves = Moves('https://pokeapi.co/api/v2/pokemon')
results = moves.extract

r = PokemonMoves(pokemon_name='bulbasaur', move_name='razor-wind', move_id='https://pokeapi.co/api/v2/move/13/',
                 level_learned_at=0, move_learn_method='egg', version_group='gold-silver')

with create_session() as session:
    session.add(r)
    session.commit()
