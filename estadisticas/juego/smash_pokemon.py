import requests
from django.shortcuts import render

def smash_pokemon(request):
    pokemon_name = request.GET.get('pokemon_name')
    
    # Realizar solicitud a la API de Pokémon para obtener más información, incluida la URL del artwork
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')
    if response.status_code == 200:
        data = response.json()
        # Obtener la URL del artwork del Pokémon
        pokemon_image_url = data['sprites']['other']['official-artwork']['front_default']
    else:
        # Si no se puede obtener la URL del artwork, establecerla como None
        pokemon_image_url = None
    
    return render(request, 'estadisticas/pokemon_smash.html', {'pokemon_name': pokemon_name, 'pokemon_image_url': pokemon_image_url})
