from django.core.management.base import BaseCommand
from estadisticas.models import Pokemon
import requests

class Command(BaseCommand):
    help = 'Carga datos de Pokémon en la base de datos'

    def handle(self, *args, **kwargs):
        # Obtener los nombres de los Pokémon
        pokemon_names = self.get_pokemon_names()

        # Obtener las estadísticas de los Pokémon
        for name in pokemon_names:
            stats = self.get_pokemon_stats(name)

            # Crear una instancia del modelo Pokemon con los datos obtenidos
            pokemon = Pokemon(
                Name=name,
                HP=stats['HP'],
                Attack=stats['Attack'],
                Defense=stats['Defense'],
                Special_Attack=stats['Special_Attack'],
                Special_Defense=stats['Special_Defense'],
                Speed=stats['Speed'],
                Element=stats['Element']
            )

            # Guardar el objeto Pokemon en la base de datos
            pokemon.save()

        self.stdout.write(self.style.SUCCESS('Datos de Pokémon cargados correctamente.'))

    def get_pokemon_names(self):
        url = 'https://pokeapi.co/api/v2/pokemon?limit=1025'
        response = requests.get(url)
        data = response.json()
        pokemon_names = [result['name'] for result in data['results']]
        return pokemon_names

    def get_pokemon_stats(self, name):
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        data = response.json()

        stats = {
            'HP': data['stats'][0]['base_stat'],
            'Attack': data['stats'][1]['base_stat'],
            'Defense': data['stats'][2]['base_stat'],
            'Special_Attack': data['stats'][3]['base_stat'],
            'Special_Defense': data['stats'][4]['base_stat'],
            'Speed': data['stats'][5]['base_stat'],
            'Element': self.get_pokemon_element(data['types'])
        }
        return stats

    def get_pokemon_element(self, types):
        url = types[0]['type']['url']
        response = requests.get(url)
        data = response.json()
        return data['name']