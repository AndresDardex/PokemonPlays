from django.shortcuts import render
import pandas as pd
from estadisticas.models import Pokemon
from random import sample
import requests

estadisticas_csv = pd.read_csv('Docs\Estadisticas.csv')
dict_estadisticas = estadisticas_csv.set_index('Name')[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total', 'Type 1']].to_dict()


import requests

def Estadisticas(request):
    # Obtener tres pokemones aleatorios de la base de datos
    random_pokemons = sample(list(Pokemon.objects.all()), 3)
    
    # Obtener el número de cada Pokémon y construir la URL del artwork
    for pokemon in random_pokemons:
        # Realizar solicitud a la API de Pokémon
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.Name.lower()}')
        if response.status_code == 200:
            data = response.json()
            # Obtener el número del Pokémon
            pokemon_number = data['id']
            # Construir la URL del artwork del Pokémon
            artwork_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{pokemon_number}.png'
            # Actualizar el objeto Pokemon con la URL del artwork
            pokemon.artwork_url = artwork_url
            pokemon.save()
        else:
            # Si no se puede obtener el número del Pokémon, manejar el error de alguna manera
            pass
    
    return render(request, 'estadisticas/index.html', {'random_pokemons': random_pokemons})



