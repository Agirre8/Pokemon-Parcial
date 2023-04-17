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

      #creamos los objetos pokemon con los elementos del csv
      pokemon = Pokemon(id, name, weapon_type, health, attack, defense)
      print(str(pokemon))
      list_of_pokemons.append(pokemon)

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



def main():


  print("Welcome to the Game.")
  print("Let's start to set the configuration of each game user. \n")

  # Get configuration for Game User 1.
  lista1 = obtener_csv_como_lista_de_diccionarios("coach_1_pokemons.csv")

  # Get configuration for Game User 2.
  lista2 = obtener_csv_como_lista_de_diccionarios("coach_2_pokemons.csv")

  print("------------------------------------------------------------------")
  print("The Game starts...")
  print("------------------------------------------------------------------")

  # Get a copy of the list of pokemons:


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
