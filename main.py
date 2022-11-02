import httpx
import json

d = httpx.get('https://pokeapi.co/api/v2/pokedex/1').json()
region = d.get('main_region').get("name")
generation = d.get('name')
for i in d.get('pokemon_species'):
    print(i.get("name"))