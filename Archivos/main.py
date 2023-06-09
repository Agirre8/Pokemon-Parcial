import os
import sys
from pokemon import Pokemon
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
        print("eliminando pokemon")

  return list_of_pokemons



def coach_is_undefeated(list_of_pokemons):
    
    while len(list_of_pokemons) != 0:
      return False
    else:
      return True
  
def choose_pokemons(list_of_pokemons):
  
  starter_pick = random.choice(list_of_pokemons)
  print(f"El pokemon seleccionado aleatoriamente es: {starter_pick.get_pokemon_name()}")
  return starter_pick

def choose_first_turn(pokemon1, pokemon2):
  lista = [pokemon1, pokemon2]
  starter_pokemon = random.choice(lista)

  return starter_pokemon

def combate(pokemon1, pokemon2):
  turno = 1
  while int(pokemon1.get_health_points()) > 0 and int(pokemon2.get_health_points()) > 0:
    if  turno % 2 != 0:
      pokemon1.fight_attack(pokemon2)
      print(f"{pokemon1.get_pokemon_name()} usó {pokemon1.get_weapon_type()} sobre {pokemon2.get_pokemon_name()}")
      turno += 1
#      print(pokemon1.get_health_points())
#      print(pokemon2.get_health_points())
    else:
      pokemon2.fight_attack(pokemon1)
      print(f"{pokemon2.get_pokemon_name()} usó {pokemon2.get_weapon_type()} sobre {pokemon1.get_pokemon_name()}")
      turno += 1
#      print(pokemon1.get_health_points())
#      print(pokemon2.get_health_points())

  print(f"\n El combate ha durado {turno} turnos")
  if pokemon1.get_health_points() > pokemon2.get_health_points():
    pokemon_ganador = pokemon1
  else:
    pokemon_ganador = pokemon2
  print(f"\n El pokemon ganador es {pokemon_ganador.get_pokemon_name()}")

  return pokemon_ganador
  

def main():

  print("Welcome to the Game.")
  print("Let's start to set the configuration of each game user. \n")

  # Get configuration for Game User 1.
  lista1 = obtener_csv_como_lista_de_diccionarios("CSV/coach_1_pokemons.csv")
  print("User1 esta preparado para la batalla")
  # Get configuration for Game User 2.
  print("------------------------------------------------------------------")
  lista2 = obtener_csv_como_lista_de_diccionarios("CSV/coach_2_pokemons.csv")
  print("User2 esta preparado para la batalla")


  print("------------------------------------------------------------------")
  print("The Game starts...")
  print("------------------------------------------------------------------")

#Los entrenadores seleccionan su primer pokemon

  starter_1 = choose_pokemons(lista1)

  starter_2 = choose_pokemons(lista2)
  
  print(f"\nUser1 opens with {starter_1.get_pokemon_name()}")
  print(f"\nUser2 opens with {starter_2.get_pokemon_name()}")

#Se escoge aleatoriamente que entrenador va ha empezar a luchar

  first_turn_pokemon = choose_first_turn(starter_1, starter_2)
  print(f"\n{first_turn_pokemon.get_pokemon_name()} is attacking first")


  # Main loop.

  vida_pokemons_1 = []
  vida_pokemons_2 = []
  while True:

    pokemon_ganador = combate(starter_1, starter_2)
    if pokemon_ganador == starter_1:
      vida_pokemons_1.append(starter_1.get_health_points())
      lista2.remove(starter_2)
      print(f"El pokemon pertenece a la lista 1")
      if len(lista2)!=0:
        starter_2 = choose_pokemons(lista2)
      else:
        print("El entrenador 2 se quedo sin Pokemons, el entrenador 1 GANA!")
        break

    else:
      vida_pokemons_2.append(starter_2.get_health_points())
      lista1.remove(starter_1)
      print(f"El pokemon pertenece a la lista 2")
      if len(lista1)!=0:
        starter_1 = choose_pokemons(lista1)
      else:
        print("El entrenador 1 se quedo sin Pokemons, el entrenador 2 GANA!")
        break


  print("------------------------------------------------------------------")
  print("The Game has end...")
  print("------------------------------------------------------------------")


  print("------------------------------------------------------------------")
  print("Statistics")
  print("------------------------------------------------------------------")
  print("Game User 1:")

  if len(vida_pokemons_1) == 0:
    print("No ha sovrevivido ningun pokemon del User1")
  else:
    print(f"Los pokemons del User1 que han sobrevivido lo han hecho con estos puntos de vida: {vida_pokemons_1}")

  print("\nGame User 2:")
  if len(vida_pokemons_1) == 0:
    print("No ha sovrevivido ningun pokemon del User2")
  else:
    print(f"Los pokemons del User2 que han sobrevivido lo han hecho con estos puntos de vida: {vida_pokemons_2}\n")



if __name__ == "__main__":
    main()


# EOF
