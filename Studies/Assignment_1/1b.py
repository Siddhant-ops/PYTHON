# Write a program to calculate sum of a digit of a number

in_num = int(input("Enter a number : "))

sum = 0
while in_num != 0:
    sum += int(in_num % 10)
    in_num /= 10

print(sum)