from random import randint
from random import shuffle

mylists = [1, 2, 3, 4]


for num in range(10):
    print(num)

print("\n================================================================================================\n")

# range() has 3 parameters
# range(start, stop, step)

for i in range(0, 10, 2):
    print(i)


# new
print("\n================================================================================================\n")
# we can use the range() and store the output as a list and display it

a = list(range(0, 11, 2))
print(a)

# new
print("\n================================================================================================\n")

index_count = 0

for letter in "abcde":
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1


# new
# enumerate() it will print a tuple which contains index no. along with its element

print("\n================================================================================================\n")

word = "Hero"

for i in enumerate(word):
    print(i)

# we can also print only letter

print("\n================================================================================================\n")

word = "Hero"

for (index, letter) in enumerate(word):
    print(letter)

# we can also print them differently

print("\n================================================================================================\n")

word = "Hero"

for (index, letter) in enumerate(word):
    print(index)
    print(letter)
    print("\n")

# new
# zip function zips together different lists and makes them tuples in result
print("\n================================================================================================\n")

mylist_1 = [1, 2, 3]
mylist_2 = ["a", "b", "c"]
mylist_3 = [100, 200, 300]

for item in zip(mylist_1, mylist_2, mylist_3):
    print(item)

print("\n================================================================================================\n")

# we can also make a list of the zip()

print(list(zip(mylist_1, mylist_2, mylist_3)))

print("\n================================================================================================\n")

# in operator will check if the parameter is in the given list, set, dictionaries, string.

print("x" in ["x", "y", "z"])
# this will return True a boolean value

print("\n================================================================================================\n")

print("x" in [1, 3, 4, 5])
# this will return false, since there is no x in the given list

# new
print("\n================================================================================================\n")

# min() will find the minimum element
# max() will find the maximum of the list

my_list = [10, 20, 30, 40]

print(min(my_list))
# this will print 10 since this the minimum value present in the given list

print(max(my_list))
# this will print 40 since this is the maximum value in the given list


# new
print("\n================================================================================================\n")

# now we are importing shuffle() from "random" library which is a built-in library

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
shuffle(new_list)
# this function will shuffle the value of the list

print(new_list)

# new
print("\n================================================================================================\n")

# now importing randint() from random library

# it returns random integer in range [a, b], including both end points.

print(randint(0, 100))

print(randint(-100, 0))

# new
print("\n================================================================================================\n")

# input() will take input from user

a = input("Whatis your name ? \n")
if a == "Lucifer":
    print("Devil knows")
elif a == "siddhant":
    print("Your birthdate is 12/03/2002")
else:
    print("wrong name")
