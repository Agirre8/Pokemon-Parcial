from pokemon import Pokemon
import random

def obtener_csv_como_lista_de_diccionarios(nombre_archivo):
    separador = ","
    with open(nombre_archivo, encoding="utf-8") as archivo:

        list_of_pokemons = []
        for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(separador)
            id = int(columnas[0])
            name = columnas[1]
            weapon_type = columnas[2]
            health = int(columnas[3])
            attack = int(columnas[4])
            defense = int(columnas[5])

            pokemon = Pokemon(id, name, weapon_type, health, attack, defense)
            print(str(pokemon))
            list_of_pokemons.append(pokemon)
        print(len(list_of_pokemons))
        pokemon1 = random.choice(list_of_pokemons)
        print(str(pokemon1))
    return list_of_pokemons

obtener_csv_como_lista_de_diccionarios("coach_1_pokemons.csv")