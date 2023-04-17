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

  



    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """



def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """


def main():

  lista1 = get_data_from_user("coach_1_pokemons.csv")
  lista2 = get_data_from_user("coach_2_pokemons.csv")

  print(lista1)
  print(lista2)

  print("Welcome to the Game.")
  print("Let's start to set the configuration of each game user. \n")

  # Get configuration for Game User 1.


  # Get configuration for Game User 2.


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
