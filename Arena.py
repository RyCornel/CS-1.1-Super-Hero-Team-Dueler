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

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())

        return hero