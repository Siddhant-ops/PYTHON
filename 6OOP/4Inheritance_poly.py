# INHERITANCE

# ========================================================================

print("\n================================================================================================\n")


class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def __init__(self):
        # this is will also execute the __init__ method of animal class
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Whoof")


myanimal = Animal()

mydog = Dog()

mydog.who_am_i()

mydog.eat()

mydog.bark()


# ========================================================================

# Polymorphism

print("\n================================================================================================\n")


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Whoof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Meow!"


niko = Dog("Niko")

felix = Cat("Felix")

print(niko.speak())

print(felix.speak())

# or we can use for loop

print("\n================================================================================================\n")

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

# or we can create and use another function

print("\n================================================================================================\n")


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)

pet_speak(felix)

# =================================================================================

# abstract Classes:
# It is never meant to be substantiated, Never expect to create an instance of this class
# it is only designed to serve as a base class

print("\n================================================================================================\n")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract Method")


# this will give you an error because abstract class is only meant to be a base class
# myanimal = Animal("Fred")


class Dog(Animal):
    def speak(self):
        return self.name + " says Whoof!"


class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"


fido = Dog("Fido")

isis = Cat("Isis")

print(fido.speak())

print(isis.speak())

