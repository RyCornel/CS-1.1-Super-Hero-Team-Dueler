from Ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        randomish = random.randint(self.max_damage // 2, self.max_damage)
        return randomish