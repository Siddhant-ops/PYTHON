# Write a python program which uses selection control statements.

num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))
num3 = float(input("Enter number 3 : "))
num4 = float(input("Enter number 4 : "))


def check_min(num1, num2, num3, num4):
    if (num1 < num2) and (num1 < num3) and (num1 < num4):
        print(f"Number {num1} is the smallest of the given input")
    elif (num2 < num3) and (num2 < num4):
        print(f"Number {num2} is the smallest of the given input")
    elif num3 < num4:
        print(f"Number {num3} is the smallest of the given input")
    else:
        print(f"Number {num4} is the smallest of the given input")


check_min(num1, num2, num3, num4)