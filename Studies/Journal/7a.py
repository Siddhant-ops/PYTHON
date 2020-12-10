# Write a python program to write and read a text file

with open("newtext.txt", "w") as f:
    f.write("This is first line")

a = ["\nthis is second append line", "\nThis is third append line"]

with open("newtext.txt", "a") as f:
    f.writelines(a)


with open("newtext.txt", "r+") as f:
    for i in f.readlines():
        print(i)
