# Accept a number from user and find whether the number is even or odd.

in_num = float(input("Enter a number : "))

print(f"The input number {in_num} is EVEN" if in_num % 2 == 0 else f"The input number {in_num} is ODD")