import random

# armor.py
class Armor:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block


    def block(self):
        block = random.randint(0, self.max_block)

        return block


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Ability", 20)
    print(armor.name)
    print(armor.block())
