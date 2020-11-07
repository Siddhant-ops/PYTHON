# MAP function
# =================================================
# map function takes two arguments:
# 1> is the function which we need to execute
# 2> is the iterable items which need to be executed by the function
# map function makes it easy for us
# its an alternative to for loop

# syntax of map():
#  map( name_of_function , name_of_iterable_items )

print("\n================================================================================================\n")

print("Map Function")
print("New")

# here we made a function which will return the square of the number


def square_num(num):
    return num ** 2


# here is the list which contains the items need to be execute in the function
my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n================================================================================================\n")

map(square_num, my_nums)

# this will print the location of the map on computer's memory

print(map(square_num, my_nums))

# in order to print the item of the map:
# there are two ways

print("\n================================================================================================\n")

# 1> using a simple for loop:
for items in map(square_num, my_nums):
    print(items)

print("\n================================================================================================\n")

# 2> making a list of those items:
print(list(map(square_num, my_nums)))

print("\n================================================================================================\n")


def slicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


name = ["Rajak", "Amisha", "Shivam", "Yashasvi", "Nancy"]

for it in map(slicer, name):
    print(it)

print("\n================================================================================================\n")

print(list(map(slicer, name)))

print("\n================================================================================================\n")

# FILTER function

# =======================================================

# filter function is similar to map function
# filter functions returns the values which are true with the given condition

print("Filter Function")
print("New")

print("\n================================================================================================\n")


def check_even(numb):
    return numb % 2 == 0


mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(filter(check_even, mynums))

print("\n================================================================================================\n")

for things in filter(check_even, mynums):
    print(things,)

print("\n================================================================================================\n")

print(list(filter(check_even, mynums)))

print("\n================================================================================================\n")


# =====================================================

# LAMBDA EXPRESSIONS

# lambda expressions are those functions which we don't use many times, that's why we write those funcs in short with the help of lambda expressions

print("Lambda Expressions")
print("New")

print("\n================================================================================================\n")

# this is how we write a default function


def square(num):
    result = num ** 2
    return result


print(square(3))

print("\n================================================================================================\n")

# following is the way to write a LAMBDA EXPRESSION

# while writing a lambda expression
# 'lambda' keyword replaces 'def function_name'
# then we pass the parameters without parentheses and then a semicolon ' : '
# we simply write the code which needs to be executed without a 'return' keyword
# and then assign a var to that expression


def square(numb):
    return numb ** 2


print(square(5))

print("\n================================================================================================\n")

print("Lambda function with Map function")

print(list(map(lambda numb: numb ** 2, mynums)))

print("Filter function with Map function")

print(list(filter(lambda nums: nums % 2 == 0, mynums)))
