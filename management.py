# Base class
class Pet:
    def __init__(self, name, age):
        self.name = name       # public attribute
        self._age = age        # protected attribute

    def speak(self):
        return "Some sound"

    def get_info(self):
        return f"{self.name} is {self._age} years old."


# Derived class 1
class Dog(Pet):
    def speak(self):
        return "Woof! Woof!"


# Derived class 2
class Cat(Pet):
    def speak(self):
        return "Meow!"


# Demonstrating encapsulation (using getter and setter)
class Fish(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.__species = species  # private attribute

    def get_species(self):
        return self.__species

    def set_species(self, new_species):
        self.__species = new_species

    def speak(self):
        return "Blub blub!"


# Polymorphism in action
def pet_sounds(pets):
    for pet in pets:
        print(f"{pet.name} says: {pet.speak()}")


# Main program
if __name__ == "__main__":
    dog = Dog("Buddy", 4)
    cat = Cat("Whiskers", 2)
    fish = Fish("Goldie", 1, "Goldfish")

    print(dog.get_info())
    print(cat.get_info())
    print(f"{fish.get_info()} Species: {fish.get_species()}")

    pets = [dog, cat, fish]
    pet_sounds(pets)
