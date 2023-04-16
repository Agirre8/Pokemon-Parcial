from weapon_type import *

class Pokemon():

    id_list = []

    def __init__(self, id, name, weapon_type, health, attack, defense):

        self.id = id
        self.weapon_type = weapon_type
        
        if len(name) == 0:
            raise ValueError("El nombre tiene que ser un string no nulo")
        else:
            self.name = name
          
        #La función isinstance() comprueba si el objeto (primer argumento) es una instancia o subclase de la clase classinfo (segundo argumento).

        if health < 1 or health > 100:
            raise ValueError("Health tiene que ser un número entre 1 y 100.")
        else:
            self.health = health
        
        if attack < 1 or attack > 10:
            raise ValueError("La fuerza del ataque tiene que estar entre 1 y 10.")
        else:
            self.attack = attack
        if defense < 1 or defense > 10:
            raise ValueError("La defensa tiene que estar entre 1 y 10.")
        else:
            self.defense = defense

        Pokemon.id_list.append(self.id)

    #GETTERS
    def get_id(self):
        return self.id

    def get_pokemon_name(self):
        return self.name

    def get_health_points(self):
        return self.health

    def get_attack_rating(self):
        return self.attack

    def get_weapon_type(self):
        return self.weapon_type

    def get_defense_rating(self):
        return self.defense

    #SETTERS
    def set_name(self, name):
        if len(name) == 0:
            raise ValueError("El nombre tiene que ser un string no nulo")
        else:
            self.name = name

    def set_health(self, health):
        if health < 1 or health > 100:
            raise ValueError("Health tiene que ser un número entre 1 y 100.")
        self.health = health

    
    def set_attack(self, attack):
        if attack <= 0:
            raise ValueError("El ataque tiene que ser un número positivo")
        self.attack = attack
  
    def set_defense(self, defense):
        if defense <= 0:
            raise ValueError("La defensa tiene que ser un valor positivo")
        self.defense = defense

    #METODO PARA COMPROBAR SI SIGUE VIVO
    def is_alive(self):
        return self.health > 0

    # METODO DE ATAQUE POKEMON
    def fight_attack(self, pokemon_to_attack):
        points_of_damage = self.attack
        return pokemon_to_attack.fight_defense(points_of_damage)

    #METODO DE DEFENSE POKEMON
    def fight_defense(self, points_of_damage):
        
        if self.defense > points_of_damage:
            return False
        else:
            self.health -= points_of_damage - self.defense
            return True

    def __del__(self):
        Pokemon.id_list.remove(self.id)

    def __str__(self):
        return f"Pokemon ID {self.id} with name {self.name} has as weapon {self.weapon_type} and health {self.health}."

def main():

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)
    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")

# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
