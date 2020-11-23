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

        for ability in self.abilities:
            total += ability.attack()
            print("Attack" %total)
            return total 


if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.name)
    print(hero.current_health)
    print(hero.abilities)

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)




