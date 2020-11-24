from Hero import Hero

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
        
    