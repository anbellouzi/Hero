class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_time = sleep_duration

    def sleep(self):
        print("{} sleeps for {} hours".format(self.name,self.sleep_time))

    def eat(self):
        print('{} is eating!'.format(self.name))

    def drink(self):
        print('{} is drinking!'.format(self.name))




class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


if __name__ == "__main__":
    dog = Dog("Sophie", 12)
    dog.sleep()
    dog.bark()
    dog.eat()
    dog.drink()
