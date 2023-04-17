import os
import sys
from pokemon import Pokemon
from pokemon_air import PokemonAir
from pokemon_earth import PokemonEarth
from pokemon_electricity import PokemonElectricity
from pokemon_water import PokemonWater
import random
import csv


def obtener_csv_como_lista_de_diccionarios(nombre_archivo):
  list_of_pokemons = []
  separador = ","

  with open(nombre_archivo, encoding="utf-8") as archivo:

    for linea in archivo:
      linea = linea.rstrip("\n")  # Quitar salto de línea
      columnas = linea.split(separador)
      id = int(columnas[0])
      name = columnas[1]
      weapon_type = columnas[2]
      health = int(columnas[3])
      attack = int(columnas[4])
      defense = int(columnas[5])

      #creamos los objetos pokemon con los elementos del csv
      pokemon = Pokemon(id, name, weapon_type, health, attack, defense)
      list_of_pokemons.append(pokemon)
      print(str(pokemon))

  return list_of_pokemons



def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

  for pokemon in list_of_pokemons:
    if pokemon.get_health_points() <= 0:
        list_of_pokemons.pop(pokemon)

  return list_of_pokemons



def coach_is_undefeated(list_of_pokemons):
    
    while len(list_of_pokemons) != 0:
      return False
    else:
      return True
  
def choose_first_pokemons(list_of_pokemons):
  
  starter_pick = random.choice(list_of_pokemons)

  return starter_pick

def choose_first_turn(pokemon1, pokemon2):
  lista = [pokemon1, pokemon2]
  starter_pokemon = random.choice(lista)

  return starter_pokemon



def main():


  print("Welcome to the Game.")
  print("Let's start to set the configuration of each game user. \n")

  # Get configuration for Game User 1.
  lista1 = obtener_csv_como_lista_de_diccionarios("coach_1_pokemons.csv")
  print("User1 esta preparado para la batalla")
  # Get configuration for Game User 2.
  print("------------------------------------------------------------------")
  lista2 = obtener_csv_como_lista_de_diccionarios("coach_2_pokemons.csv")
  print("User2 esta preparado para la batalla")


  print("------------------------------------------------------------------")
  print("The Game starts...")
  print("------------------------------------------------------------------")

#Los entrenadores seleccionan su primer pokemon

  starter_1 = choose_first_pokemons(lista1)

  starter_2 = choose_first_pokemons(lista2)
  
  print(f"\nUser1 opens with {starter_1.get_pokemon_name()}\n")
  print(f"User2 opens with {starter_2.get_pokemon_name()}\n")

#Se escoge aleatoriamente que entrenador va ha empezar a luchar


  first_turn_pokemon = choose_first_turn(starter_1, starter_2)
  print(f"{first_turn_pokemon.get_pokemon_name()} is attacking first\n")


  # Choose first pokemons


  # Main loop.



  print("------------------------------------------------------------------")
  print("The Game has end...")
  print("------------------------------------------------------------------")


  print("------------------------------------------------------------------")
  print("Statistics")
  print("------------------------------------------------------------------")
  print("Game User 1:")


  print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
