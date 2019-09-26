from random import randint, choice

# TODO: Function to handle incorrect user input and conver to int as right now its NOT dry

def int_input(txt):
    try:
        val = int(input())
    except Exception:
        return 0

    return val

class Arena:
    def __init__(self):
        self.team_one = Team('Team 1')
        self.team_two = Team('Team 2')

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What do you want the name of the ability to be?")
        max_damage = int_input("What is the max damage you want the ability to have?") # Defaults to 0

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What do you want the name of the weapon to be?")
        max_damage = int_input(
            "What is the max damage that you want the weapon to have?")
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        name = input("What do you want the name of the armor to be?")
        max_block = int_input("How much damage do you want it to absorb?")
        return Armor(name, max_block)

    def create_hero(self):
        # Getting name and basic health
        # TODO: Number checking
        name = input(
            "welcome to the hero creator! What do you want the name of your hero to be?")
        health = int_input("Great name! Would you like to change the default hp of your character? (default: 100)")

        hero = Hero(name, health)

        add_abilities = input(
            "Awesome! Would you like to add some abilities? (y/n)")
        if 'y' in add_abilities:
            #TODO: Refactor
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)
                another_ability = input(
                    "Would you like to add another ability? (y/n)")
                if "y" not in another_ability:
                    break

        add_weapons = input(
            "Nice abilities!  Would you like to add some weapons to your hero? (y/n)")
        if 'y' in add_weapons:
            while True:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                another_weapon = input(
                    "Would you like to add another weapon? (y/n)")
                if "y" not in another_weapon:
                    break

        add_armor = input(
            "Those weapons seem deadly.  Finally, would you like to add some armor? (y/n)")
        if 'y' in add_armor:
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)
                another_armor = input(
                    "Would you like to add some more armor? (y/n)")
                if "y" not in another_armor:
                    break

        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        num_of_heros = int_input("Welcome to the team one builder! How many heros would you like to add to team one?")

        for i in range(num_of_heros):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build two '''
        num_of_heros = int_input("Welcome to the team two builder! How many heros would you like to add to team two?")
        for i in range(num_of_heros):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        self.team_one.stats()
        self.team_two.stats()

        # TODO: Team stats display
        # if team_one_stats > team_two_stats:
        #     print(f"Team one wins with a KD Ratio of {team_one_stats}")
        #     print(f"Team one's surviving heros are as followed: ")
        #     for hero in self.team_one.heroes:
        #         if hero.current_health > 0:
        #             print(hero.name)
        # elif team_two_stats > team_one_stats:
        #     print(f"Two two wins with a KD ratio of {team_two_stats}")
        #     print(f"Team two's surviving heros are as followed: ")
        #     for hero in self.team_one.heroes:
        #         if current_health > 0:
        #             print(hero.name)


class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
            name: String
            max_damage: Integer
        '''
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        '''Return a value between 0 and value set my self.max_damage'''
        return randint(0, self.max_damage)


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        half = self.max_damage // 2
        return randint(half, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Return a random value between 0 and the initialized max_block strength.'''
        return randint(0, self.max_block)


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        '''Battle each team against each other'''
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            local_hero = choice(self.alive_heroes())
            enemy_hero = choice(other_team.alive_heroes())
            local_hero.fight(enemy_hero)

    def alive_heroes(self):
        return [x for x in self.heroes if x.is_alive()]

    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            hero.hero_stats()


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        '''Add ability object to abilities:List'''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def add_kills(self, num_kills):
        '''Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def defend(self, damage_amt=0):
        '''Runs `block` method on each armor.
            Returns sum of all blocks
        '''
        total = 0
        for armor in self.armors:
            block_val = int(armor.block())
            total += block_val
        return abs(total - damage_amt)

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        curr_hp = self.current_health
        dmg_after_def = self.defend(damage)
        self.current_health = curr_hp - dmg_after_def

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0

    def hero_stats(self):
        if self.deaths > 0:
            kd = self.kills // self.deaths
            print(f"Hero: {self.name} had a KD ratio of {kd}")
        else:
            print(f"Hero: {self.name} had a KD ratio of {self.kills}")

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in. (Attacker has advantage)
        '''
        # while self.is_alive() and opponent.is_alive():
        while True:
            if self.is_alive():  # Check if self is still alive
                self_dmg = self.attack()  # Get attack damage
                opponent.take_damage(self_dmg)  # Enemy takes dmg
            else:  # Breaks out of loop and sends msg if self gets killed
                print(
                    f'{opponent.name} emerged the victor after being challenged to a duel!')
                opponent.add_kills(1)
                self.add_deaths(1)
                break

            if opponent.is_alive():  # Check if opponent is still alive
                opp_dmg = opponent.attack()  # Enemy attacks
                self.take_damage(opp_dmg)  # Self takes dmg
            else:  # Breaks out of loop and sends msg if opponent gets killed
                print(f'{self.name} started the fight and won!')
                self.add_kills(1)
                opponent.add_deaths(1)
                break


if __name__ == "__main__":
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
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
