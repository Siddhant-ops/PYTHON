# Write a program to generate Fibonacci series

def fibb():
    # Program to display the Fibonacci sequence up to n-th term

    nterms = int(input("How many terms do you want to print ? "))

    # first two terms
    num_1, num_22 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print(f"Fibonacci sequence upto {nterms} :")
        print(num_1)
    else:
        print("Fibonacci sequence :")
        while count < nterms:
            print(num_1)
            # update values
            num_1, num_22 = num_22, (num_1 + num_22)
            count += 1

fibb()