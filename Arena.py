from Ability import Ability
from Weapon import Weapon
from Armor import Armor
from Hero import Hero
from Team import Team


class Arena:
    def __init__(self):
        self.team_uno = Team("Team-Uno")
        self.team_dos = Team("Team-Dos")

    def create_ability(self):
        name = input("What is the ability name?")
        max_damage = input("What is the max damage of the ability?")

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name?")
        max_damage = input("What is the max damage of the weapon?")

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name?")
        max_strength = input("What is the max strength of the armor?")

        return Armor(name, max_strength)