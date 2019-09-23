import random
class Ability:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        attack = random.randint(0, self.attack_strength)
        return attack


import random
class Armor:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block


    def block(self):
        block = random.randint(0, self.max_block)
        return block


# Superheros.py
class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100):
        self.name = name
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.starting_health = starting_health



    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)


    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        # TODO: This method should run Ability.attack() on every ability
        # in self.abilities and returns the total as an integer.
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()

        return damage

    def defand(self, damage_amt):
        '''Runs `block` method on each armor. Returns sum of all blocks'''
        # TODO: This method should run the block method on each armor in self.armors
        sum = 0

        if armors:
            for armor in armors:
                sum += armor.block()


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
