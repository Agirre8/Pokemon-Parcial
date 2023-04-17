import csv
import sys
import os
from pokemon import Pokemon
"""
def get_data_from_user(name_file):
    with open(name_file, 'r') as csv_file:
        csv_reader = reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        print(list_of_rows)
"""


def get_data_from_user1(name_file):

    list_of_pokemons = []
    separador = ","
    with open(name_file, encoding="utf-8") as archivo:

        for linea in archivo:  
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(separador)
            id = columnas[0]
            name = columnas[1]
            weapon_type = columnas[2]
            health = columnas[3]
            attack = columnas[4]
            defense = columnas[5]

            pokemon = Pokemon(id, name, weapon_type, health, attack, defense)
    
    list_of_pokemons.append(Pokemon)
    print(list_of_pokemons)

get_data_from_user1("coach_1_pokemons.csv")