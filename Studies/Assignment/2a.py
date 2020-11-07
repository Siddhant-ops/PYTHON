# Write a program to calculate factorial of a number. Accept number from user.

def fact():
    in_num = int(input("Enter a number : "))
    factorial = 1
    if in_num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif in_num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,in_num + 1):
            factorial = factorial*i
        print(f"The factorial of {in_num} is {factorial}")

fact()