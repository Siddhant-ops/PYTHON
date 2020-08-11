print("================================================================================================")

# Lets import math

import math

# help(math)

# let's see how to round numbers

value = 4.35

print(value)

# floor function returns absolute value < 'x'

value = math.floor(value)

print("==================================================")

print(value)

print("==================================================")

value = 4.67

# ceilling function returns absolute value > 'x'

value = math.ceil(value)

print(value)

print("================================================================================================")

# round method will round-up the numbers

# But there are some rules of that

# let's assume we have to round-up 'a' which is 'x.5' where 'x' can be any number

# 1> if 'x' is odd no., then result of round-up is 'x + 1' which is > 'x.5' . result cannot be any odd no.s 1, 3, 5, 7

# 1> if 'x' is even no., then result of round-up is 'x' which is < 'x.5' . result would be 0, 2, 4, 6, 8

print(round(4.5))

print("==================================================")

print(round(5.5))

print("================================================================================================")

print(math.pi)

print("================================================================================================")

print(math.e)

print("================================================================================================")

print(math.inf)

print("================================================================================================")

print(math.log(100, 10))

print("================================================================================================")

print(10 ** 3)

print("================================================================================================")

print(math.sin(70))

print("================================================================================================")

print(math.degrees(math.pi / 2))

print("================================================================================================")

print(math.radians(100))

print("================================================================================================")

# If ur math operations are really intense and consists huge numbers, you can use numpy library, it is highly efficient and goes much deeper than PYTHON's built-in library

# ====================================================================

import random

# This returns a random integer within a given range which are passed on as arguments

my_random_int = random.randint(0, 100)

print(my_random_int)

print("================================================================================================")

# Seeding allows us to start from a seated pseudo random number generator, which means the same random numbers in a series

# now the random.randint() function will display the same number repeatedly

random.seed(42)

rand = random.randint(0, 100)

print(rand)

print("================================================================================================")

mylist = list(range(0, 20))

print(mylist)

print("==================================================")

#  this is a way to randomly choose an element from a sequence

print(random.choice(mylist))

print("==================================================")

# this is a way to randomly choose elements from a sequence

# This method is gonna print elements which have the possiblty of being repeated

# With replacement
print(random.choices(population=mylist, k=10))

print("==================================================")

# Without replacement
print(random.sample(population=mylist, k=10))

print("================================================================================================")

# now let's shuffle our list

random.shuffle(mylist)

print(mylist)

print("================================================================================================")

# A uniform random distribution is function in which u enter ur args which are range and when it's executed, it outputs a random numberfrom that range. Since all the numbers in that range have the same probability to be chosen. It randomly choses for you. (It's floating point)

print(random.uniform(0, 100))

print("================================================================================================")

print(random.gauss(0, 1))
