# Tuples are mutable or immutable? Justify with the help of a program.

# tuple is an immutable data type.
# we cannot edit it, once it's declared and intialized
# we can make changes to it and assign a new tuple

mytuple = (19, 45, 24, 60, 56, 38, 21, 78, 31, 5, 49, 57)

mytuple[0] = 3

# TypeError: 'tuple' object does not support item assignment
