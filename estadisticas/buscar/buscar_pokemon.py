# views.py
import requests
from django.shortcuts import render
from ..models import Pokemon

def buscar_pokemon(request):
    if 'pokemon_buscado' in request.GET:
        nombre_pokemon = request.GET['pokemon_buscado']
        # Buscar el Pokémon en la base de datos
        try:
            # Cambia 'nombre' a 'Name' en la consulta para que coincida con el campo de la base de datos
            pokemon = Pokemon.objects.get(Name=nombre_pokemon)
            
            # Realizar solicitud a la API de Pokémon para obtener más información, incluido el artwork
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}')
            if response.status_code == 200:
                data = response.json()
                # Obtener la URL del artwork del Pokémon
                artwork_url = data['sprites']['other']['home']['front_default']
            else:
                # Si no se puede obtener la URL del artwork, establecerla como None
                artwork_url = None

            # Renderizar la página con los detalles del Pokémon y la URL del artwork
            return render(request, 'estadisticas/pokemon_base.html', {'pokemon': pokemon, 'artwork_url': artwork_url})
        except Pokemon.DoesNotExist:
            mensaje = 'El Pokémon no fue encontrado.'
            return render(request, 'estadisticas/error.html', {'mensaje': mensaje})
    else:
        mensaje = 'Por favor, introduce un nombre de Pokémon.'
        return render(request, 'estadisticas/error.html', {'mensaje': mensaje})
