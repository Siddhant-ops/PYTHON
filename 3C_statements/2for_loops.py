# for loops
# they iterate elements
# syntax of for loop

#my_iterable = [1,2,3];
# for item_name in my_iterable:
# print(item_name)

name = "Siddhant"

for i in name:
    print(i)

# it will print
# S
# i
# d
# d
# h
# a
# n
# t

print('================================================================================================')

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in mylist:
    print(i)

print('================================================================================================')

# we can execute any code in response to for i in mylist:

for i in mylist:
    print("hey there")

print('================================================================================================')

# we can print even and odd no.s from mylist

for i in mylist:
    if i % 2 == 0:
        print("The No. {} is EVEN".format(i))
    else:
        print("The No. {} is ODD".format(i))

print('================================================================================================')

# new
listsum = 0

for i in mylist:
    listsum += i

print(listsum)

print('================================================================================================')

# this prints total sum = 45

# new
listsum = 0

for i in mylist:
    listsum = listsum + i
    print(listsum)

print('================================================================================================')

# this prints
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45

print('================================================================================================')

# new

mystring = "Siddhant Dalvi"

for letter in mystring:
    print(letter)

# this will print Siddhant Dalvi Letter by letter in new line and it will include the blank space also
# S
# i
# d
# d
# h
# a
# n
# t
#
# D
# a
# l
# v
# i

print('================================================================================================')

# Advanced people in python, when they want to iterate a thing they simply use a _ (underscore) as a variable_name/item name

for _ in "Siddhant":
    print("Cool!")

print('================================================================================================')

# new

# we can also print tuples with for loop

mytuple = (1, 2, 3, 4)

for item in mytuple:
    print(item)

print('================================================================================================')

# new

# tuple packing and unpacking
# if we are iterating through a sequence that contains itself tuples the item can be used with tuple unpacking

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]

# lenght of the list = 4
print(len(mylist))

for item in mylist:
    print(item)

# it will print the content of the list which are 4 tuples
# output wil be
# (1,2)
# (3,4)
# (5,6)
# (7,8)

print('================================================================================================')

# in order to also print the content of the tuples which are inside the lists, we can do the following

for (a, b) in mylist:
    print(a)
    print(b)

# this will print the contents of the tuples seperately
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# we can also use it to print only single values from the tuples

for (a, b) in mylist:
    print(b)

print('================================================================================================')

# new

mylist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in mylist:
    print(b)

# this will only print 2,5,8 which the 'b'represents in the tuples

print('================================================================================================')

# new

# we can also use for loops to display the values of a dictionary

d = {'k1': 1, "k2": 2, 'k3': 3}

for items in d:
    print(items)

# this will only print:
# k1
# k2
# k3

print('================================================================================================')

# in order to display it clearly

d = {'k1': 1, "k2": 2, 'k3': 3}

for items, value in d.keys():
    print({item: value})

# this will print :
#('k1', 1)
#('k2', 2)
#('k3', 3)

print('================================================================================================')

# in order to display the values of the keys we should :

d = {'k1': 1, "k2": 2, 'k3': 3}

for key, value in d.items():
    print(value)

# this will print thhe values of the key

# 1
# 2
# 3

print('================================================================================================')

# Or we can also do the following

d = {'k1': 1, "k2": 2, 'k3': 3}

for value in d.values():
    print(value)

# this will print thhe values of the key

# 1
# 2
# 3
