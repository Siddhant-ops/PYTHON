# Create a class Square with two methods to compute area and perimeter of square
# respectively. Accept inputs from user.


class Square:
    def __init__(self, side):
        self.side = side

    def square_area(self):
        print(f"Area of the square is { format((self.side ** 2), '.3f') }")

    def square_perimeter(self):
        print(f"Perimeter of the square is { format((self.side * 4), '.3f') }")


side = float(input("Enter side of square : "))
s = Square(side)

s.square_area()
s.square_perimeter()
