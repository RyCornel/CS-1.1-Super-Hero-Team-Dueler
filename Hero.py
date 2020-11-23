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


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)




