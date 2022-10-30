from pokeapidash.requests.requester import Requester
from pokeapidash.models.pokemon import PokemonPokemon
import httpx

result = httpx.get('https://pokeapi.co/api/v2/pokemon/606/').json()


class Pokemon(Requester):
    @staticmethod
    def get_status(status: dict) -> dict:
        status = {stat.get('stat').get('name'): stat.get('base_stat') for stat in status}
        names = {'hp': 'hp', 'attack': 'attack', 'defense': 'defense',
                 'special-attack': 'special_attack', 'special-defense': 'special_defense',
                 'speed': 'speed'}
        return dict((names[key], value) for (key, value) in status.items())

    def get_info(self, result: dict) -> list:
        id = result.get('id')
        name = result.get('name')
        weight = result.get('weight')
        height = result.get('height')
        back_default = result.get('sprites').get('back_default')
        front_default = result.get('sprites').get('front_default')

        stats = self.get_status(result.get('stats'))

        return [
            PokemonPokemon(id=id, pokemon_name=name, **stats, weight=weight, height=height, back_sprite=back_default,
                           front_sprite=front_default)]
