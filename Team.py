from Hero import Hero
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False

        for Hero in self.heroes:
            if Hero.name == name:
                self.heroes.remove(Hero)
                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        print([Hero for Hero in self.heroes])

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def stats(self):
        for Hero in self.heroes:
            kd = Hero.kills / Hero.deaths
            print(f"{Hero.name} Kill/Deaths: {kd}")

    def revive_heroes(self, health = 100):
        for Hero in self.heroes:
            Hero.current_health = health

    def attack(self, other_team):

        living_heores = list()
        living_opponents = list()

        for Hero in self.heroes:
            living_heores.append(Hero)

        for Hero in other_team.heroes:
            living_opponents.append(Hero)

        while len(living_heores) > 0 and len(living_opponents) > 0:
        
            hero1 = random.choice(living_heores)
            hero2 = random.choice(living_opponents)
            
            hero1.fight(hero2)

            if hero1.is_alive():
                living_opponents.remove(hero2)
            else:
                living_heores.remove(hero1)
    