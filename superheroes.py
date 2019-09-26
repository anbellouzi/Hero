from random import randint, choice
import random

# check if user input is a int value
def input_number(user_input):
    try:
       val = int(user_input)
    except ValueError:
       return 0
    return val

# arena class
class Arena:
    def __init__(self):
        self.team_one = Team("Team 1")
        self.team_two = Team("Team 2")

    # create ability for a hero
    def create_ability(self):
        ability_name = input("Name an ability you would like to add to your hero: ")
        max_damage = input_number(input("Enter ability max damage: "))
        ability = Ability(ability_name, max_damage)
        return ability

    # create weapon for a hero
    def create_weapon(self):
        weapon_name = input("Name a weapon you would like to add to your hero: ")
        max_damage = input_number(input("Enter weapon max damage: "))
        weapon = Weapon(weapon_name, max_damage)
        return weapon

    # create armor for a hero
    def create_armor(self):
        armor_name = input("Name an armor you would like to add to your hero: ")
        max_block = input_number(input("Enter armor max block: "))
        armor = Armor(armor_name, max_block)
        return armor

    # create a hero
    def create_hero(self):
        # creating hero
        hero_name = input("Name for a hero: ")
        health = input_number(input("Enter hero starting health or leave blank for default(100): "))
        if health == 0:
            hero = Hero(hero_name)
        else:
            hero = Hero(hero_name, health)

        print("")
        ability_1 = input("Would you like to add abilities to your hero: y/n ")
        if 'y' in ability_1.lower():
            print("Adding abilities for {} ....".format(hero.name))
            print("")
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)
                ability_2 = input("Would you like to add another ability to your hero: y/n ")
                if "n" in ability_2.lower():
                    break

        print("")
        armor_1 = input("Would you like to add armors to your hero: y/n ")
        if 'y' in armor_1.lower():
            print("Adding armor for {} ....".format(hero.name))
            print("")
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)
                armor_2 = input("Would you like to add another armor to your hero: y/n ")
                if "n" in armor_2.lower():
                    break

        return hero

    # create team one
    def build_team_one(self):
        number_of_heroes = input_number(input("How many Heroes you would like on team one: "))
        for count in range(number_of_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # create team two
    def build_team_two(self):
        number_of_heroes = input_number(input("How many Heroes you would like on team two: "))
        for count in range(number_of_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    # team one attacks team two
    def team_battle(self):
        print("__________________________")
        print("Battle begins...")
        self.team_one.attack(self.team_two)

    # Display both teams stats
    def show_stats(self):
        print()
        print("Heroes stats:")
        print("__________________________")
        self.team_one.stats()
        self.team_two.stats()
        print("__________________________")
        print()

    def print_list(self):
        print(self.team_one.heroes)

# ability class
class Ability:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        attack = randint(0, self.max_damage)
        return attack

# weapon class
class Weapon(Ability):

    def attack(self):
        half_power = self.max_damage // 2
        return randint(half_power, self.max_damage)

# armor class
class Armor:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block


    def block(self):
        block = randint(0, self.max_block)
        return block

# Team class
class Team:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name):
        self.name = name
        self.heroes = []

    # adds a hero to heroes list
    def add_hero(self, hero):
        print("")
        print("adding hero {} to {}".format(hero.name, self.name))
        print("")
        self.heroes.append(hero)

    # remove a hero from heroes list
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def live_heroes(self):
        heroes_alive = []
        if self.heroes:
            for hero in self.heroes:
                if hero.current_health > 0:
                    heroes_alive.append(hero)

            return heroes_alive

    # Keep all your current code, but add these methods
    def attack(self, other_team):
        while len(self.live_heroes()) > 0 and len(other_team.live_heroes()) > 0:
            local_hero = choice(self.live_heroes())
            enemy_hero = choice(other_team.live_heroes())
            print("{} is fighting {}".format(local_hero.name, enemy_hero.name))
            local_hero.fight(enemy_hero)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.set_current_health = health

    def stats(self):
        if self.heroes:
            for hero in self.heroes:
                hero.show_stats()

# hero class
class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0
        print("")
        print("{} hero is created with HP: {}".format(name, self.current_health))

    # update kills
    def add_kill(self, num_kills):
        self.kills += num_kills
        if num_kills == 1:
            print("{} Added {} kill".format(self.name, num_kills))
        else:
            print("{} Added {} kills".format(self.name, num_kills))

    # update deaths
    def add_death(self, num_deaths):
        self.deaths += num_deaths
        if num_deaths == 1:
            print("{} Added {} death".format(self.name, num_deaths))
        else:
            print("{} Added {} deaths".format(self.name, num_deaths))

    # add ability
    def add_ability(self, ability):
        self.abilities.append(ability)
        print("")
        print("{} added ability {} with max_damage: {}".format(self.name, ability.name, ability.max_damage))
        print("")

    # add weapons to self.abilities
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print("{} added weapon: {}".format(self.name, weapon.name))

    # add armors to self.armors
    def add_armor(self, armor):
        self.armors.append(armor)
        print("")
        print("{} added armor {} with max_block: {}".format(self.name, armor.name, armor.max_block))
        print("")

    # setter for updating current health
    def set_current_health(self, new_health):
        self.current_health = new_health

    # returns the value of current health
    def get_current_health(self):
        return self.current_health

    # getter for armors
    def get_armors(self):
        return self.armors

    # getter for abilities
    def get_abilities(self):
        return self.abilities

    # getter for name
    def get_name(self):
        return self.name


    def is_alive(self):
        return self.current_health > 0

    # display hero stats to console
    def show_stats(self):
        if self.deaths > 0:
            ratio = self.kills // self.deaths
            print("{} has ratio of {} kills/deaths".format(self.name, ratio))
        else:
            print("{} has ratio of {} kills/deaths".format(self.name, self.kills))


    def attack(self):
        total_damage = 0
        if self.get_abilities():
            for ability in self.get_abilities():
                total_damage += ability.attack()

        else:
            print(self.get_name()+" has no abilities!")

        return total_damage

    def defend(self, damage=0):
        total_armors = 0
        if self.get_armors():
            for armor in self.get_armors():
                total_armors += int(armor.block())

        return abs(total_armors - damage)

    def take_damage(self, damage):


        current_hp = self.current_health
        damage_after_defend = self.defend(damage)
        self.current_health = current_hp - damage_after_defend
        print("{} took {} damage, damage after defend is {} and {}'s new health is {}".format(self.name, damage, damage_after_defend, self.name, self.current_health))


    def fight(self, opponent):

        while self.is_alive() and opponent.is_alive():

            self_damage = self.attack()
            print("")
            print("{} attacked {} with damage amount {}".format(self.name,opponent.name ,self_damage))
            opponent.take_damage(self_damage)

            opponent_damage = opponent.attack()
            print("")
            print("{} attacked {} with damage amount {}".format(opponent.name, self.name,opponent_damage))
            self.take_damage(opponent.attack())

            if opponent.is_alive() == False:
                print("")
                print(self.get_name()+" Won!")
                self.add_kill(1)
                print("{} is dead".format(opponent.name))
                opponent.add_death(1)


            elif(self.is_alive() == False):
                print("")
                print(opponent.get_name()+" Won!")
                opponent.add_kill(1)
                print("{} is dead".format(self.name))
                self.add_death(1)



def test_one():
    flash = Hero("Flash", 120)
    flash_ability = Ability("Speed", 50)
    flash_armor = Armor("Shield", 10)
    flash.add_ability(flash_ability)
    flash.add_armor(flash_armor)

    arrow = Hero("Arrow", 150)
    arrow_armor = Armor("sheild", 20)
    arrow_ability = Ability("Arrows", 50)
    arrow.add_ability(arrow_ability)
    arrow.add_armor(arrow_armor)

    while flash.is_alive() and arrow.is_alive():
        flash.fight(arrow)

    flash.show_stats()
    arrow.show_stats()



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    # test_one()

    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
