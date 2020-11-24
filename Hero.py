from Ability import Ability
from Armor import Armor
from Weapon import Weapon
import random

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    
    def fight(self, opponent):
        if (opponent.abilities == []) and (self.abilities == []):
            print("Draw")

        else: 
            while self.current_health and opponent.current_health >= 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                
            if self.is_alive() == True:
                print(f"{self.name} is the winner")
                self.add_kill += 1
                opponent.add_death += 1
                    
            else: 
                print(f"{opponent.name} is the winner")
                opponent.add_kill += 1
                self.add_death +=1


    def add_weapon(self, weapon):
        self.abilities.append(weapon)


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

    
    def add_kill(self, num_kills):
        self.kills += num_kills


    def add_death(self, num_deaths):
        self.deaths += num_deaths
    
#------------------Tests--------------------#

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero1.add_weapon(weapon)
    print(hero1.attack())
   




