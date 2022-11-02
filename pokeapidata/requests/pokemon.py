from pokeapidata.requests.requester import Requester
from pokeapidata.models.pokemon import PokemonPokemon


class Pokemon(Requester):
    @staticmethod
    def get_status(status: dict) -> dict:
        status = {stat.get('stat').get('name'): stat.get('base_stat') for stat in status}
        names = {'hp': 'hp', 'attack': 'attack', 'defense': 'defense',
                 'special-attack': 'special_attack', 'special-defense': 'special_defense',
                 'speed': 'speed'}
        return dict((names[key], value) for (key, value) in status.items())

    @staticmethod
    def get_type(types: dict) -> dict:
        return {f"type_{type.get('slot')}": type.get('type').get('name') for type in types}

    def get_info(self, result: dict) -> list:
        id = result.get('id')
        name = result.get('name')
        base_experience = result.get('base_experience')
        weight = result.get('weight')
        height = result.get('height')
        back_default = result.get('sprites').get('back_default')
        front_default = result.get('sprites').get('front_default')

        stats = self.get_status(result.get('stats'))
        types = self.get_type(result.get('types'))
        return [
            PokemonPokemon(id=id, pokemon_name=name, **stats, weight=weight, height=height, back_sprite=back_default,
                           front_sprite=front_default, **types)]
