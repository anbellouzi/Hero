import ability

# Superheros.py
class Hero:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, starting_health=100):
        self.name = name
        self.current_health = starting_health

    abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)
        pass


    def attack():
        pass

    def defend(incoming_damage):
        pass

    def take_damage(damage):
        pass

    def is_alive():
        pass

    def fight(opponent):
        pass




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = ability.Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)
