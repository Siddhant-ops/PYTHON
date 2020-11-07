# Write a function to check whether a number is Armstrong or not. Accept number from user.

def check_A():
    in_num = int(input("Enter a number : "))
    sum = 0
    tem = in_num
    while tem > 0:
        digit = tem % 10
        sum += digit ** 3
        tem //= 10

    print(f"{in_num} is an Armstrong Number" if in_num == sum else f"{in_num} is not an Armstrong Number")

check_A()