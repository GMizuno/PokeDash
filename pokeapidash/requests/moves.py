from pokeapidash.models.move import PokemonMoves
from pokeapidash.requests.requester import Requester


class Moves(Requester):

    def get_info(self, result: dict) -> list:
        moves = []
        poke_name = result.get('name')
        for x in result.get('moves'):
            move_name = x.get('move').get('name')
            url = x.get('move').get('url')
            for i in x.get('version_group_details'):
                level_learned_at = i.get('level_learned_at')
                move_learn_method = i.get('move_learn_method').get('name')
                version_group = i.get('version_group').get('name')
                moves.append(PokemonMoves(poke_name, move_name, url, level_learned_at, move_learn_method, version_group))
        return moves

