print("\n================================================================================================\n")


# Execute various operations of tuple in python and display output.

t = tuple(range(100, 120))

print(f"Printing a tuple : {t}")


print("\n================================================================================================\n")


# Accessing a tuple

print(f"Accessing a tuple : {t[7]}")


print("\n================================================================================================\n")


# SLicing a tuple and printing it

print(f"SLicing a tuple and printing it : {t[-13:-5:2]}")


print("\n==================================================\n")


# SLicing a tuple and assigning it to new variable

new_t = t[7:15]
print(f"SLicing a tuple and assigning it to new variable : {new_t}")


print("\n================================================================================================\n")


# Reassigning a tuple

# t[5] = "hello"

# TypeError: 'tuple' object does not support item assignment. Tuples are immutable. Their values cannot be changed.


# methods on tuple

new_tup = ("one", 2, "three", 2, 3, 4, 2, 2)

# count() method will count the no. of particular element in the tuple
print(f"Count Method : {new_tup.count(2)}")


print("\n==================================================\n")


# index() method will show the first index no. of an element
print(f"Index Method : {new_tup.index(2)}")


print("\n================================================================================================\n")


# Nested tuples

my_tuple = (1, 2, 3, 5, 6, 7, ("hello", 124.14, 214, 752), "awesome")
print(f"Nested Tuple : {my_tuple[[6][0] :]}")


print("\n================================================================================================\n")


# Operations on Tuples

# Membership

print(f"Membership : {'hello' in my_tuple}")


print("\n==================================================\n")


# Iterating through a Tuple

for i in my_tuple:
    print(f"Iterating a tuple : {i}")


print("\n==================================================\n")


# Concatenation of tuples

tup_add = my_tuple + new_tup
print(f"Concatenation : {tup_add}")


print("\n================================================================================================\n")

# Repitition

new_tuple = tuple(("hii",) * 4)
print(f"Repititon : {new_tuple}")


print("\n================================================================================================\n")

# Built-in Functions on tuples :

# Maximum

print(f"Maximum : {max(t)}")


print("\n==================================================\n")


# Minimum

print(f"Minimum : {min(t)}")


print("\n==================================================\n")


# length of tuple

print(f"Length of a tuple : {len(my_tuple)}")


print("\n==================================================\n")


# tuple method converts a sequence into a tuple

print(f"Converting a sequence into a tuple : {tuple(range(0,10))}")


print("\n==================================================\n")


# Sorting
mytuple = (344, 1516, 1141, 2547, 978234, 98, 812, 9129, 98234)
print(sorted(mytuple))


print("\n==================================================\n")


# Enumerate
x = enumerate(mytuple)
for i in x:
    print(f"Enumerate : {i}")


print("\n================================================================================================\n")


# deleting a tuple

del t

print(t)
