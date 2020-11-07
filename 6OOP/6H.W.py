# Object Oriented Programming

# Homework Assignment

# Problem 1

# Fill in the Line class methods to accept coordinates as a pair of tuples
# and return the slope and distance of the line

# class Line:
#
#   def __init__(self,coor1,coor2):
#       pass
#
#   def distance(self):
#       pass
#
#   def slope(self):
#       pass

print("\n================================================================================================\n")
print("Distance and Slope of a line")


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        self.dist = (((self.coor2[0] - self.coor1[0]) ** 2) + ((self.coor2[1] - self.coor1[1]) ** 2)) ** (1 / 2)
        return f"Distance of the line is {self.dist}"

    def slope(self):

        self.slop = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return f"Slope of the line is {self.slop}"


line = Line((1, 2), (4, 3))

print(line.distance())
print(line.slope())

# new

# Problem 2

# Fill in the class

# class Cylinder:
#
#    def __init__(self,height=1,radius=1):
#        pass
#
#    def volume(self):
#        pass
#
#    def surface_area(self):
#        pass

print("\n================================================================================================\n")
print("Volume and Surface Area of a Cylinder")


class Cylinder:

    pi = 3.14

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        self.vol = self.height * Cylinder.pi * (self.radius) ** 2
        return f"Volume of a Cylinder is {self.vol}"

    def surface_area(self):
        self.sa = (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius) ** 2)
        return f"Surface Area of a Cylinder is {self.sa}"


cylin = Cylinder(2, 5)

print(cylin.volume())
print(cylin.surface_area())
