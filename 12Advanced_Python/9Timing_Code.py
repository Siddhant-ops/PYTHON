print("================================================================================================")

# As we will further learn advanced methods we would have to learn to best implement the code which compiles the fastest

# we can check the fastest solution by the following ways:

# 1> simply tracking time elapsed

# 2> using timeit module

# 3> Special %%timeit "magic" for jupyter Notebooks

# 1st

# I'll make a function which return a list of numbers converted to string


def func_one(n):
    return [str(num) for num in range(n)]


print(func_one(10))

print("==================================================")


def func_two(n):
    return list(map(str, range(n)))


print(func_two(10))

print("================================================================================================")

# both give the same output but we need to know which solution is most effective in terms of timing

# to calculate time we can use time module

import time

# for func_one


def func_1_time():

    # we have to simply find current time before

    start_time = time.time()

    # Now we will run the code with a big arg of 1000000

    result = func_one(1000000)

    # current time after running the code

    end_time = time.time()

    # elapsed time

    elapsed = end_time - start_time

    print(elapsed)


func_1_time()

print("==================================================")

# for func_two


def func_2_time():

    # we have to simply find current time before

    start_time = time.time()

    # Now we will run the code with a big arg of 1000000

    result = func_two(1000000)

    # current time after running the code

    end_time = time.time()

    # elapsed time

    elapsed = end_time - start_time

    print(elapsed)


func_2_time()

print("================================================================================================")

# Now we will use timeit module

import timeit

stmt = """
func_one(100)
"""

setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""

# this is goin to run the function 100000 time

# for func_one

print(timeit.timeit(stmt, setup, number=1000000))

print("==================================================")

# for func_two

stmt = """
func_two(100)
"""

setup = """
def func_two(n):
    return list(map(str, range(n)))
"""

# this is goin to run the function 100000 time

print(timeit.timeit(stmt, setup, number=1000000))

print("================================================================================================")
