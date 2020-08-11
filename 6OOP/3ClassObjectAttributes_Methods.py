print("================================================================================================")


class Dog:

    # Class Object Attribute
    # Same for any instance of a class
    species = "Mammal"

    # __init__ acts a constructor
    # self acts a reference to the instance of the class
    def __init__(self, mybreed, name, spots):

        # Attributes
        # we take in the argument
        # Assign it using self.attribute_name based on the parameters
        self.mybreed = mybreed
        self.name = name
        self.spots = spots

    # OPERATIONS/Actions ------> METHODS
    def bark(self, number):
        print("WOOF! My name is {} and my number is {}".format(self.name, number))


mydog = Dog(mybreed="Lab", name="Sam", spots=False)

print(mydog.mybreed)

print("==================================================")

print(mydog.name)

print("==================================================")

print(mydog.spots)

print("==================================================")

print(mydog.species)

print("==================================================")

print(mydog.bark(3))

print("================================================================================================")

# Methods are essentially functions defined inside the body of the class
# and they are used to perform operations
# that sometimes utilize the actual attributes

# Basically methods are as functions acting on an object
# that take object itself into account through the use of the self argument or self keyword.

# ========================================================================


class Circle:

    # Class Object Attribute
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # method
    def get_circumference(self):
        return self.radius * Circle.pi * 2


# if we want to change value of radius from 1 to 30
# pass the argument 30 in Circle(30)

mycircle = Circle(30)

print(mycircle.pi)
print(mycircle.radius)
print(mycircle.get_circumference())
print(mycircle.area)

