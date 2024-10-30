# Parent class (or base class)
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def print_information(self):
        print(f"{self.name}")
# Child class (or derived class) inheriting from Anima
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} says Woof!"
# Create an instance of the Dog class
dog = Dog("Buddy")
# Call the speak method of the Dog class

print(dog.speak())
-------------------------------------
VERSION II

# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Parent class inheriting from Animal
class Mammal(Animal):
    # No need for an extra speak method here if it doesn't add new behavior
    pass

# Child class inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Woof!"

# Create an instance of the Dog class
dog = Dog("Buddy")

# Call the speak method of the Dog class
print(dog.speak())

-------------------------

# HIERARCHICAL Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Child class 1 inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Child class 2 inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Create instances of the Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method of the Dog and Cat instances
print(dog.speak())
print(cat.speak())

_________________________________________________________

# MUltiple inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Intermediate class inheriting from Animal
class Mammal(Animal):
    def speak(self):
        pass


# Child class 1 inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Woof!"


# Child class 2 inheriting from Mammal
class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"


# Create instances of the Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method of the Dog and Cat instances
print(dog.speak())
print(cat.speak())
'''