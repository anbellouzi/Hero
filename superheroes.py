from random import randint, choice
import random

# ability class
class Ability:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        attack = random.randint(0, self.max_damage)
        return attack

# armor class
class Armor:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block


    def block(self):
        block = random.randint(0, self.max_block)
        return block

# weapon class
class Weapon(Ability):

    def attack(self):
        half_power = self.max_damage // 2
        return random.randint(half_power, self.max_damage)

# Team class
class Team:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name):
        self.name = name
        self.heroes = []

    # adds a hero to heroes list
    def add_hero(self, hero):
        self.heroes.append(hero)

    # remove a hero from heroes list
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)


    # Keep all your current code, but add these methods
    def attack(self, other_team):

        while True:
            my_live_heroes = self.live_heroes()
            other_live_heroes = other_team.live_heroes()

            if len(my_live_heroes) > 0 and len(other_live_heroes) > 0:
                my_hero = choice(my_live_heroes)
                opponent = choice(other_live_heroes)
                my_hero.fight(opponent)
            else:
                return False



    def live_heroes(self):
        heroes_alive = []
        for hero in self.heroes:
            if hero.is_alive():
                heroes_alive.append(hero)
        return heroes_alive

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.set_current_health = health

    def stats(self):
        for hero in heroes:
            hero.show_stats()

# hero class
class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100, health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    # update kills
    def add_kill(self, num_kills):
        self.kills += num_kills

    # update deaths
    def add_death(self, num_deaths):
        self.deaths += num_deaths

    # add weapons to self.abilities
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    # add armors to self.armors
    def add_armor(self, armor):
        self.armors.append(armor)

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

    # add ability
    def add_ability(self, ability):
        self.abilities.append(ability)

    # add armors
    def add_armor(self, armor):
        self.armors.append(armor)

    # display hero stats to console
    def show_stats(self):
        if self.deaths > 0:
            ratio = self.kills // self.deaths
            print("{} has {} ratio of kills/deaths".format(self.name, ratio))
        else:
            print("{} has ratio kills/deaths of {}".format(self.name, self.kills))


    def attack(self):
        total_damage = 0
        abilities = self.get_abilities()
        if abilities:
            for ability in self.abilities:
                total_damage += ability.attack()

        else:
            print(self.get_name()+" has no abilities!")

        return total_damage

    def defend(self, damage_amt=0):
        total_armors = 0
        armors = self.get_armors()
        if armors:
            for armor in armors:
                total_armors += armor.block()

        return abs(total_armors - damage_amt)

    def take_damage(self, damage):
        new_health = self.get_current_health() - self.defend(damage)
        self.set_current_health(new_health)

    def is_alive(self):
        if self.get_current_health() <= 0:
          return False
        else:
          return True


    def fight(self, opponent):
        while True:
            if self.get_abilities() and opponent.get_abilities():
                if self.is_alive():
                    opponent.take_damage(self.attack())
                else:
                    print(opponent.get_name()+" Won!")
                    self.add_death(1)
                    opponent.add_kill(1)
                    return False

                if opponent.is_alive():
                    self.take_damage(opponent.attack())
                else:
                    print(self.get_name()+" Won!")
                    opponent.add_death(1)
                    self.add_kill(1)
                    return False
            else:
                print("Draw")
                return False

# arena class
class Arena:
    def __init__(self):
        self.team_one = Team("Team 1")
        self.team_two = Team("Team 2")

    # check if user input is a int value
    def input_number(user_input):
        try:
           val = int(user_input)
        except ValueError:
           print("That's not an int!")
           return 0
        return val

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
        hero_name = input("Name you would like to give to hero: ")
        health = input_number(input("Enter hero starting health or leave blank for default(100): "))
        hero = Hero(hero_name, health)
        return hero


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 8000)
    ability4 = Ability("Wizard Beard", 2000)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
