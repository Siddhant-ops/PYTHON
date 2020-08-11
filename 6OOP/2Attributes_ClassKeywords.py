mylist = [1, 2, 3]

myset = set()

print(type(myset))

print(type(mylist))


class Dog:
    # __init__ acts a constructor
    # self acts a reference to the instance of the class
    def __init__(self, mybreed, name, spots):

        # Attributes
        # we take in the argument
        # Assign it using self.attribute_name based on the parameters
        self.mybreed = mybreed
        self.name = name
        self.spots = spots


mydog = Dog(mybreed="DobberMan", name="Max", spots=True)

print(type(mydog))

print(mydog.mybreed)
print(mydog.name)
print(mydog.spots)

print("================================================================================================")

mydog2 = Dog("lab", "drake", True)

print(mydog2.mybreed)
print(mydog2.name)
print(mydog2.spots)
