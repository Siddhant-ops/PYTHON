# Write a program to implement method overriding in python

from math import pi


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Square):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def fact(self):
        return "Circle has no angle."


a = Square(4)
b = Circle(7)
print(b.fact())
print(a.fact())
print(b.area())
print(a.area())
