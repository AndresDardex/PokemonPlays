from django.contrib import admin
from estadisticas.models import Pokemon

def guardar_pokemones(diccionario_pokemones):
    for estadisticas, nombre in diccionario_pokemones.items():
        pokemon = Pokemon.objects.create(
            Name=nombre,
            HP=estadisticas['HP'],
            Attack=estadisticas['Attack'],
            Defense=estadisticas['Defense'],
            Special_Attack=estadisticas['Special Attack'],
            Special_Defense=estadisticas['Special Defense'],
            Speed=estadisticas['Speed'],
            Element=estadisticas['Element']
        )
        pokemon.save()


class EstadisticasAdmin(admin.ModelAdmin):
    list_display = ['Name', 'HP', 'Attack', 'Defense', 'Special_Attack', 'Special_Defense', 'Speed', 'Element']
    search_fields = ['Name']
    
admin.site.register(Pokemon, EstadisticasAdmin)