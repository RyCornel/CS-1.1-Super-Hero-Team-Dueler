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
        if (opponent.abilities == []) and (self.abilities == []):
            print("Draw")

        else: 
            while self.current_health and opponent.current_health >= 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                
            if self.is_alive() == True:
                print(f"{self.name} is the winner")
                    
            else: 
                print(f"{opponent.name} is the winner")


        


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
        injured = damage - self.defend()
        self.current_health -= injured 


    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True  

    
#------------------Tests--------------------#

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Seed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
   




