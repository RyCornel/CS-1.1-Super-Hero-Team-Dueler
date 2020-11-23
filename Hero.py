from Ability import Ability
from Armor import Armor
import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
    
    def fight(self, opponent):
        self.opponent = opponent
        hero1 = opponent
        hero2 = opponent
        fighters = (hero1, hero2)
        print(random.choice(fighters))

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        damage_amount = 0

        for ability in self.abilities:
            damage_amount += ability.defend()
            return damage_amount

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()


    def is_alive(self):
        if current_health <= 0:
            return False
        else:f
            return True  


if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.name)
    print(hero.current_health)
   




