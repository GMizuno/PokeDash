from pokeapidata.models.version import PokemonVersion
import httpx


class Version:

    def __init__(self, urls: list) -> None:
        self.urls = urls
    @property
    def extract(self):
        data = []
        for url in self.urls:
            data += self.get_data(url)
        return data

    def get_data(self, url: str) -> list:
        info = httpx.get(url).json()
        return self.get_info(info)

    def get_info(self, info: dict) -> list:
        data = []
        region = info.get('main_region').get("name")
        generation = info.get('name')
        for i in info.get('pokemon_species'):
            data.append(PokemonVersion(generation=generation, region=region, pokemon_name=i.get("name")))
        return data
