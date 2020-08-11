# decorators allow youto decorate a function

# python has decorators that allow you to tack on extra
# functionalitymto analready existing function

# they use the @ operator andare then placed on top
# of the original function

# there are 2 parts on learning decorators
# 1> nested functions
# 2> Using decorators with @ operators

print("==================================================================")


def func():
    print(1)


func()

print(func)
# this prints out the information of the function
# whereit's situated in the memory

print("==================================================================")


def hello():
    print("hello!")


hello()

greet = hello

greet()

print("==================================================================")

# now u must be thinking did greet pointed to hello
# or did greet made a copy of hello

# we can easily check that out if it is pointing to hello
# by deleting hello

del hello

# now let's see if we can now call greet

greet()

# so hence we know greet made a copy of hello function

print("==================================================================")


def hello(name="Sid"):
    print("the hello() function has been executed")

    def greet():
        print("\t This is greet() function inside hello")

    def welcome():
        print("\t Welcome inside hello")

    # u can write " greet() " or " print(greet()) "
    greet()
    print(greet())

    # u can write " welcome() " or " print(welcome()) "
    welcome()
    print(welcome())

    print("This is the END of the hello function")


hello()

print("==================================================================")

# since greet and welcome are defined inside of
# hello function, there scope is limited to that function
# only they cannot be called outside in a simple way,
# like welcome()

# welcome()
# this would return a NameError, Since it's defined inside the function and
# doesn't has global scope

# instead they can be called by the following method


def hello(name="Sid"):
    print("the hello() function has been executed")

    def greet():
        print("\t This is greet() function inside hello")

    def welcome():
        print("\t Welcome inside hello")

    print("I'm going to return a function")

    if name.lower() == "Sid".lower():
        return greet
    else:
        return welcome


# now in order to call greet we call,
# hello function with name as Sid in
# argument

hello("Sid")

# if we run this
# the hello() function has been executed
# I'm going to return a function

print("==================================================================")

print(hello("Sid"))

# output of this line will be:
# the hello() function has been executed
# I'm going to return a function
# <function hello.<locals>.greet at 0x000001574F580A68>

# it also shows that it is a function named hello and has a local function named greet and it's stored location in the memory

# now we will assign it to a new variable

print("==================================================================")

my_new_func = hello("Sid")

# now i'll print my_new_func var

print(my_new_func)

print("==================================================================")

# now we treat my_new_func as function and call it

my_new_func()

# or we can simply call print on it

print("==================================================================")

# hence we can call it by assigning it to a var and call it


def cool():
    def super_cool():
        print("\t I'm super cool inside cool function")

    return super_cool


# now lets assign it to a variable

some_func = cool()

some_func()

print("==================================================================")

# here i've now made a function which has an argument, this argument is the name of some other function and the main function should return the calling of the argument function


def hello():
    print("Hi Sid!")


def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())


print(hello)

hello()

print("==================================================================")

# now we will call the "other" function and it's argument will be "hello" so when "other" function is called it also calls "hello" function

other(hello)

# now we have all the tools to create our decorator

print("==================================================================")

# here "new_decorator" function is the decorator

# and "func_needs_Decorated" function is the one we would decorate now


def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the 'original' function")

        original_func()

        print("Some extra code after the 'original' function")

    return wrap_func


def func_needs_decorator():
    print("I want to be decorated")


# now we will call the "new_decorator"with argument "func_needs_decorator" and assign it to a variable

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

# it works out pretty good

print("==================================================================")

# but the following line is big and complex for some people so that's why pyhton has @ operator

# decorated_func = new_decorator(func_needs_decorator)

# we can simply do the following


@new_decorator
def func_needs_decorator():
    print("I want to be decorated")


func_needs_decorator()

# now if we ever feel like not using the decorator just comment it
