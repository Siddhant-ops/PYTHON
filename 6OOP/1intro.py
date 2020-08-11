# OBJECT ORIENTED PROGRAMMING (OOP)

# Object Oriented Programming (OOP) allows programmers
# to create thier own objects that have methods and attributes.

# Recall that after defining a string, list, dictionary or other objects,
# you werea able to call methods off of them with the .method_name() syntax.

# These methods act as functions that use information
# about the object, as well as the object itself to return
# results or change the current object.

# OOP allows users to create thier own objects

# the general format is often confusing when first encountered,
# and it's usefulness may not be completely clear at first.

# In general, OOP allows us to create code
# that is repeatable and organized.

# For much larger scripts of python code,
# functions by themselves aren't enough for organized and repeatability.

# Commonly repeated tasks and objects can be defined with OOP to create code
# that is more usable.

# Here is the syntax:


class NameOfClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)

