from bs4 import BeautifulSoup
import requests
import os
import shutil
from pprint import pprint

src = requests.get('http://pokemondb.net/pokedex/national')
soup = BeautifulSoup(src.content, 'lxml')
generation = soup.find_all('div', attrs={'class': 'infocard-list infocard-list-pkmn-lg'})
pk_name = soup.find_all('a', attrs={'class': 'ent-name'})

shutil.rmtree("pokemons")
os.mkdir("pokemons")
s = 1

for g in generation:
    os.mkdir(f"pokemons/season {s}")
    pokemons = g.find_all('div', attrs={'class': 'infocard'})
    for p in pokemons:
        pokemon_name = p.select("span.infocard-lg-data a.ent-name")[0].text
        img_url = p.select("span.infocard-lg-img a span")[0]["data-src"]
        img_content = requests.get(img_url).content
        with open(f'pokemons/season {s}/{pokemon_name}.jpg', 'wb') as f:
            f.write(img_content)
    s += 1

