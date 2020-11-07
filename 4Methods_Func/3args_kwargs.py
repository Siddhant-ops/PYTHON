# creating a function that will return 5% ofthe sum of two no.s


def sum_five_percent(a, b):
    return sum((a, b)) * 0.05


result = sum_five_percent(7, 9)
print(result)


# new
print("\n================================================================================================\n")

# we can also pass on multiple arguments


def sum_five_percent(a, b, c, d, e):
    return sum((a, b, c, d, e)) * 0.05


result = sum_five_percent(7, 9, 4, 8, 2)
print(result)


# new
print("\n================================================================================================\n")

# when we enter '*args' in the arguments of a function, while calling the function we can enter as many parameters we want and they will be accepted as a tuple
# now this tuple will be accepted in the sum()


def myfunc(*args):
    return sum(args) * 0.05


result = myfunc(70, 30)
print(result)

# new
print("\n================================================================================================\n")

# we don't have to compulsarily write *args instead of args we can write any word


def myfunc(*spam):
    return int(sum(spam) * 0.05)


result = myfunc(93, 29)
print(result)

# new
print("\n================================================================================================\n")


def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")


myfunc(fruit="apple", veggi="tomato")

# new
print("\n================================================================================================\n")

# accepting both args and kwargs


def myfunc(*args, **kwargs):
    print("I would like {} {}".format(args[1], kwargs["animal"]))


myfunc(10, 20, 30, fruit="orange", food="eggs", animal="dogs")

