# Strings are mutable or immutable? Justify with the help of a program.

# String is an immutable data type.
# we cannot edit it, once it's declared and intialized
# we can make changes to it and assign a new string

mystring = "Hey there, what's up?"

mystring[0] = "h"

# TypeError: 'str' object does not support item assignment