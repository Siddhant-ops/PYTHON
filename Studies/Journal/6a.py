import Geometry as geo


def area_circle():
    radius = float(input("Enter radius of the circle : "))
    geo.area_circle(radius)


def area_triangle():
    base = float(input("Enter base of the triangle : "))
    height = float(input("Enter height of the triangle : "))
    geo.area_triangle(base, height)


def area_square():
    side = float(input("Enter side of the square : "))
    geo.area_square(side)


def area_rect():
    length = float(input("Enter length of the rectangle : "))
    breadth = float(input("Enter breadth of the rectangle : "))
    geo.area_rect(length, breadth)


area_circle()
area_triangle()
area_square()
area_rect()
