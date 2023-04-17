import random
def choose_first_turn(pokemon1, pokemon2):
  lista = [pokemon1, pokemon2]
  starter_pokemon = random.choice(lista)
  print(starter_pokemon)

  choose_first_turn("1", "2")