import random
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
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
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


# Superheros.py
class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.abilities = list()
        self.armors = list()

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


    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        # TODO: This method should run Ability.attack() on every ability
        # in self.abilities and returns the total as an integer.
        total_damage = 0
        abilities = self.get_abilities()
        if abilities:
            for ability in self.abilities:
                total_damage += ability.attack()

        else:
            print(self.get_name()+" has no abilities!")

        return total_damage

    def defand(self, damage_amt):
        '''Runs `block` method on each armor. Returns sum of all blocks'''
        # TODO: This method should run the block method on each armor in self.armors
        total_armors = 0
        armors = self.get_armors()
        if armors:
            for armor in armors:
                total_armors += armor.block()

        return damage_amt - total_armors

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        new_health = self.get_current_health() - self.defand(damage)
        self.set_current_health(new_health)

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check whether the hero is alive and return true or false
        if self.get_current_health() <= 0:
          return False
        else:
          return True


    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Print the victor's name to the screen.
        while True:
            if self.get_abilities() and opponent.get_abilities():
                if self.is_alive():
                    opponent.take_damage(self.attack())
                else:
                    print(opponent.get_name()+" Won!")
                    return False

                if opponent.is_alive():
                    self.take_damage(opponent.attack())
                else:
                    print(self.get_name()+" Won!")
                    return False
            else:
                print("Draw")
                return False




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
