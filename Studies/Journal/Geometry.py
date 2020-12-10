# Module named Geometry

from math import pi


def area_circle(r):
    a = pi * r * r
    a = format(a, ".3f")
    print(f"Area of circle having radius : {r} is ===> {a}")


def area_triangle(b, h):
    a = (b * h) / 2
    a = format(a, ".3f")
    print(f"Area of triangle having base : {b} and height : {h} is ===> {a}")


def area_square(s):
    a = s ** 2
    a = format(a, ".3f")
    print(f"Area of square having side : {s} is ===> {a}")


def area_rect(l, b):
    a = l * b
    a = format(a, ".3f")
    print(f"Area of rectangle having length : {l} and breadth : {b} is ===> {a}")
