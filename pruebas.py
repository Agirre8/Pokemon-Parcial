from enum import Enum
import random
class WeaponType(Enum):

    PUNCH = "PUNCH"
    KICK = "KICK" 
    ELBOW = "ELBOW"
    HEADBUTT = "HEADBUTT"


class Pokemon():

    id_list = []

    def __init__(self, id, name, weapon_type, health, attack, defense):

        self.id = id
        self.weapon_type = weapon_type
        
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("El nombre tiene que ser una cadena no vacía")
        else:
            self.name = name

        if not isinstance(health, int) or health < 1 or health > 100:
            raise ValueError("La salud tiene que ser un número entre 1 y 100.")
        else:
            self.health = health

        if not isinstance(attack, int) or attack < 1 or attack > 10:
            raise ValueError("El ataque tiene que estar entre 1 y 10.")
        else:
            self.attack = attack

        if not isinstance(defense, int) or defense < 1 or defense > 10:
            raise ValueError("La defensa tiene que estar entre 1 y 10.")
        else:
            self.defense = defense

        Pokemon.id_list.append(self.id)

    def __str__(self):
        return f"Pokemon ID {self.id} con nombre {self.name}, con arma {self.weapon_type} y con salud {self.health}"

def main():
        numero_aleatorio = random.randint(0, 1)
        points_of_damage = 10

        if numero_aleatorio == 0:
            points_of_damage = points_of_damage * 2 
        else:
            pass
        print(points_of_damage)

if __name__ == "__main__":
    main()