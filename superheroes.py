from random import random, randint, choice
import time
import sys

time_01 = 0.1
time_025 = 0.25
time_050 = 0.50
time_1 = 1

# check if user input is a int value
def input_number(user_input):
    while user_input.isdigit() == False:
        user_input = input("Enter a number: ")
    return int(user_input)

# arena class
class Arena:
    def __init__(self):
        self.team_one = Team("Team 1")
        self.team_two = Team("Team 2")

    # create ability for a hero
    def create_ability(self):
        ability_name = input("Ability name: ")
        max_damage = input_number(input("Max damage number: "))
        ability = Ability(ability_name, max_damage)
        return ability

    # create weapon for a hero
    def create_weapon(self):
        weapon_name = input("Weapon name: ")
        max_damage = input_number(input("Max damage number: "))
        weapon = Weapon(weapon_name, max_damage)
        return weapon

    # create armor for a hero
    def create_armor(self):
        armor_name = input("Armor name: ")
        max_block = input_number(input("Max block number: "))
        armor = Armor(armor_name, max_block)
        return armor

    # create a hero
    def create_hero(self, count):
        # creating hero
        hero_name = ""
        if count == 1:
            hero_name = input("Name for your {}st hero: ".format(count))
        elif count == 2:
            hero_name = input("Name for your {}nd hero: ".format(count))
        elif count == 3:
            hero_name = input("Name for your {}rd hero: ".format(count))
        else:
            hero_name = input("Name for your {}th hero: ".format(count))

        if not hero_name:
            hero_name = "Hero"

        # health = input_number(input("{} starting health (default:100Health): ".format(hero_name)))
        health = input("{} starting health (default:100Health): ".format(hero_name))
        try:
           health = int(health)
           hero = Hero(hero_name, health)
        except ValueError:
            hero = Hero(hero_name)

        print("")
        ability_1 = input("Do you want create Ability to {}: y/n ".format(hero_name))
        if ('y' or "") in ability_1.lower():
            print("Creating Abilities for {} ....".format(hero.name))
            print("")
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)
                ability_2 = input("Create another Ability: y/n ")
                if "n" in ability_2.lower():
                    break
                print("")


        print("")
        weapon_1 = input("Do you want to create Weapon for {}: y/n ".format(hero_name))
        if ('y' or "") in weapon_1.lower():
            print("Creating Weapon for {} ....".format(hero.name))
            print("")
            while True:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                weapon_2 = input("Create another Weapon: y/n ")
                if "n" in weapon_2.lower():
                    break
                print("")

        print("")
        armor_1 = input("Do you want to create Armor for {}: y/n ".format(hero_name))
        if ('y' or "") in armor_1.lower():
            print("Creating Armor for {} ....".format(hero.name))
            print("")
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)
                armor_2 = input("Create another Armor: y/n ")
                if "n" in armor_2.lower():
                    break
                print("")

        return hero

    # create team one
    def build_team_one(self):
        print("")
        number_of_heroes = input_number(input("How many Heroes do you want on team one: "))
        while number_of_heroes == 0:
            print("That's not a valid input number!")
            number_of_heroes = input_number(input("How many Heroes do you want on team one: "))

        print("")
        for count in range(1, number_of_heroes+1):
            hero = self.create_hero(count)
            self.team_one.add_hero(hero)

    # create team two
    def build_team_two(self):
        print("")
        number_of_heroes = input_number(input("How many Heroes do you want on team two: "))
        while number_of_heroes == 0:
            print("That's not a valid input number!")
        print("")
        for count in range(1, number_of_heroes+1):
            hero = self.create_hero(count)
            self.team_two.add_hero(hero)


    # team one attacks team two
    def team_battle(self):
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

# Team class
class Team:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name):
        self.name = name
        self.heroes = []

    # adds a hero to heroes list
    def add_hero(self, hero):
        print("")
        hero.stack_overflow()
        self.heroes.append(hero)
        print("")
        print("{} added to {} √".format(hero.name, self.name))
        print("")
        time.sleep(time_025)


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
            print("")
            time.sleep(time_050)
            print("          Team 1          ")
            self.view_all_heroes()
            print("")
            time.sleep(time_050)
            print("          Team 2          ")
            other_team.view_all_heroes()
            print("__________________________")
            print("")
            time.sleep(time_1)

            print("OPPONENTS".format(local_hero.name, enemy_hero.name))
            time.sleep(time_050)
            print("           Hero           ")
            local_hero.show_status()
            print("")
            time.sleep(time_050)
            print("           Enemy          ")
            enemy_hero.show_status()
            print("")
            time.sleep(time_1)
            display_battle_art(local_hero.name, enemy_hero.name)
            time.sleep(time_1)
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
        print("Name: {} | Health: {}HP".format(name, self.current_health))

    def stack_overflow(self):
        # Source: https://stackoverflow.com/questions/2122385/dynamic-terminal-printing-with-python
        for i in range(10):
            sys.stdout.write("\r{0}>".format("="*i))
            sys.stdout.flush()
            time.sleep(0.1)



    def show_status(self):
        self.stack_overflow()
        print()
        print("__________________________")
        print("Name: {} | Health: {}HP".format(self.name, self.current_health))
        if self.abilities:
            for ability in self.abilities:
                if isinstance(ability, Weapon):
                    print("Weapon: {} | Max_damage: {}".format(ability.name, ability.max_damage))
                else:
                    print("Ability: {} | Max_damage: {}".format(ability.name, ability.max_damage))

        if self.armors:
            for armor in self.armors:
                print("Armor: {} | Max_Block: {}".format(armor.name, armor.max_block))
        print("__________________________")
        time.sleep(time_050)

    # update kills
    def add_kill(self, num_kills):
        self.kills += num_kills
        if num_kills == 1:
            print("{} has {} kill".format(self.name, num_kills))
        else:
            print("{} has {} kills".format(self.name, num_kills))

    # update deaths
    def add_death(self, num_deaths):
        self.deaths += num_deaths
        if num_deaths == 1:
            print("{} has {} death".format(self.name, num_deaths))
        else:
            print("{} has {} deaths".format(self.name, num_deaths))

    # add ability
    def add_ability(self, ability):
        self.abilities.append(ability)
        print("")
        self.show_status()
        print("")

    # add weapons to self.abilities
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print("")
        self.show_status()
        print("")
        # print("Hero: {} | alive(: {}".format(self.name, self.current_health))
        # print("Weapon: {} | Max_damage: {}".format(weapon.name, weapon.max_damage))

    # add armors to self.armors
    def add_armor(self, armor):
        self.armors.append(armor)
        print("")
        self.show_status()
        # print("Hero: {} | Health: {}HP".format(self.name, self.current_health))
        # print("Armor: {} | Max_block: {}".format(armor.name, armor.max_block))
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
            # print(self.get_name()+" has no abilities!")
            pass

        return total_damage

    def defend(self, damage=0):
        total_armors = 0
        if self.get_armors():
            for armor in self.get_armors():
                total_armors += int(armor.block())

        return abs(total_armors - damage)

    def take_damage(self, damage):

        if damage > 0:
            current_Health = self.current_health
            damage_after_defend = self.defend(damage)
            self.current_health = current_Health - damage_after_defend
            blocked = damage - damage_after_defend
            print("{} blocked {} hits".format(self.name, blocked))
            time.sleep(time_025)
            print("{} took {} damage hits".format(self.name, damage_after_defend))
            time.sleep(time_025)
            print("{}'s current health: {}HP".format(self.name, self.current_health))
            time.sleep(time_1)
        else:
            print("{} blocked all hits, health remains {}HP".format(self.name, self.current_health))
            time.sleep(time_1)


    def fight(self, opponent):

        while self.is_alive() and opponent.is_alive():

            self_damage = self.attack()
            print("")
            if self_damage > 0:
                print("{} attacked {} by {} damage hits".format(self.name,opponent.name ,self_damage))
                time.sleep(time_025)
            else:
                print("{} attacked {} but did no damage: {}".format(self.name,opponent.name ,self_damage))
                time.sleep(time_025)
            opponent.take_damage(self_damage)

            opponent_damage = opponent.attack()
            print("")
            if opponent_damage > 0:
                print("{} attacked {} by {} damage hits".format(opponent.name, self.name,opponent_damage))
                time.sleep(time_025)
            else:
                print("{} attacked {} but did no damage: {}".format(opponent.name, self.name,opponent_damage))
                time.sleep(time_025)
            self.take_damage(opponent.attack())

            if opponent.is_alive() == False:
                print("")
                print("                            End Fight ")
                print("")
                time.sleep(time_050)
                print(self.get_name()+" Won!")
                time.sleep(time_025)
                self.add_kill(1)
                print("{} is dead".format(opponent.name))
                time.sleep(time_025)
                opponent.add_death(1)
                time.sleep(time_050)

            elif(self.is_alive() == False):
                print("")
                print("                            End Fight")
                print("")
                time.sleep(time_1)
                print(opponent.get_name()+" Won!")
                opponent.add_kill(1)
                time.sleep(time_025)
                print("{} is dead".format(self.name))
                self.add_death(1)
                time.sleep(time_050)

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

def test_two():
    flash = Hero("Flash", 200)
    flash_ability = Ability("Speed", 50)
    flash_armor = Armor("Shield", 10)
    flash.add_ability(flash_ability)
    flash.add_armor(flash_armor)

    arrow = Hero("Arrow", 120)
    arrow_ability = Ability("Arrow", 20)
    arrow_ability2 = Ability("Box", 15)
    arrow_armor = Armor("Shield", 10)
    arrow.add_ability(arrow_ability)
    arrow.add_ability(arrow_ability2)
    arrow.add_armor(arrow_armor)


    arrow = Hero("Arrow", 150)
    arrow_armor = Armor("sheild", 20)
    arrow_ability = Ability("Arrows", 50)
    arrow.add_ability(arrow_ability)
    arrow.add_armor(arrow_armor)

    while flash.is_alive() and arrow.is_alive():
        flash.fight(arrow)

    flash.show_stats()
    arrow.show_stats()

    print(type(flash))

def display_battle_art(hero, enemy):
    print("__________________________ {} VS {} __________________________".format(hero,enemy))
    print("")
    print("                \\                                           ___/________")
    print("       ___   )                    ,  @                    /    \\  \\")
    print("    @___, \\ /                  @__\\  /\\              @___/      \\@/")
    print("   /\\__,   |                  /\\_, \\/ /             /\\__/        |")
    print("  / \\    / @\\                / \\   (               / \\ /        / \\")
    print("_/__|___/___/_______________/__|____\\_____________/__/__________|__\\__")
    print("")
    print("                            Fight Detail                            ")

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
