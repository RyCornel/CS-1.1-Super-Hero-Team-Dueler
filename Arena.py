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

    
    def build_team_uno(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_uno.add_hero(Hero)

        
    def build_team_dos(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_dos.add_hero(Hero)

    
    def team_battle(self):
        self.team_uno.attack(self.team_dos)

    
    def show_stats(self):
        print("\n")
        print(self.team_uno.name + "statistics: ")
        self.team_uno.stats()
        print("\n")
        print(self.team_dos.name + " statistics: ")
        self.team_dos.stats()
        print("\n")

        team_kills = 0
        team_deaths = 0
        for hero in self.team_uno.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_uno.name + " average K/D was: " + str(team_kills/team_deaths))
        print(self.team_dos.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_uno.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_uno.name + ": " + hero.name)

        for hero in self.team_dos.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_dos.name + ": " + hero.name)


#------------------Tests--------------------#
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_uno()
    arena.build_team_dos()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_uno.revive_heroes()
            arena.team_dos.revive_heroes()