import os
import shutil
import requests
from pprint import pprint
from bs4 import BeautifulSoup

shutil.rmtree("pokemons", ignore_errors=True)
os.mkdir("pokemons")

src = requests.get('http://pokemondb.net/pokedex/national')

soup = BeautifulSoup(src.content, 'html.parser')
generations = soup.find_all('div', attrs={'class': 'infocard-list infocard-list-pkmn-lg'})
pk_name = soup.find_all('a', attrs={'class': 'ent-name'})


s = 1
for generation in generations:
    os.mkdir(f"pokemons/season {s}")
    pokemons = generation.find_all('div', attrs={'class': 'infocard'})

    for pokemon in pokemons:
        pokemon_name = pokemon.select("span.infocard-lg-data a.ent-name")[0].text
        print(pokemon.select("span.infocard-lg-img a span"))
        img_url = pokemon.select("span.infocard-lg-img a span")[0]["data-src"]
        img_content = requests.get(img_url).content
        with open(f'pokemons/season {s}/{pokemon_name}.jpg', 'wb') as f:
            f.write(img_content)
    s += 1


