# tuples are similar to lists
# tuples are immutable

t = (1, 2, 3, 4, 5, 6, 7, 8)
print(t)

print("\n==================================================\n")

# data type of tuple
print(type(t))

print("\n================================================================================================\n")

# tuples can contain both strings and numbers
my_tuple = ("one", 2, "three", 2, 3, 4, 2, 2)
print(my_tuple)

print("\n================================================================================================\n")

# slicing and indexing can also be done in tuple

print(my_tuple[0])

print("\n==================================================\n")

print(t[0:])

print("\n==================================================\n")

print(t[1:5:2])

print("\n==================================================\n")


# count() method will count the no. of particular element in the tuple
print(my_tuple.count(2))

print("\n==================================================\n")


# index() method will show the first index no. of an element
print(my_tuple.index(2))

print("\n================================================================================================\n")



def ask(age, skill="java"):
    name = input("Enter ur name : ")
    print(f"name is {name} and {age} with skill is {skill}")

ask(16)