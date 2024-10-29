from abc import ABC, abstractmethod

class Animal(ABC):
    def describe(self):
        print("This is an animal.") #concrete method

    @abstractmethod
    def make_sound(self):
        pass              #abstract method

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

if __name__ == "__main__":
    animals = [Dog(), Cat(), Cow()]

    for animal in animals:
        animal.describe()
        print(f"The {animal.__class__.__name__} says: {animal.make_sound()}\n")