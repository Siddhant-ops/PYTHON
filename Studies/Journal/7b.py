# Write a python program to read a file line by line and store each line as an element of
# a list. Display the resultant list.

with open("newtext.txt", "r") as f:
    my_list = f.readlines()
    print(my_list)
