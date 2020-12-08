Dollar = "$"

num = int(input("Enter the number of column : "))

for i in range(1, num, +2):
    for j in range(0, i):
        print(Dollar, end=" ")
    print(end="\n")

for i in range(num, 0, -2):
    for j in range(1, i + 1, 1):
        print(Dollar, end=" ")
    print(end="\n")
