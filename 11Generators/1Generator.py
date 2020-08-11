# Generator functions allows us to write a function that can send back a value and later resume to pick up where it left off

# This type of function is a generator in Pytho, allowing us to generate a sequence of values over time instead of creating a whole sequence and hold it in memory.

# when a generator function is compiled they become an object that supports an iteration protocol

# that means when they are called in your code they don't actually return a value and then exit

# generator functions will automatically suspend and resume their execution and state around the last point of value generation

# the advantage is that instead of having to compute an entire series of value up front, the generator computes one value waits untill the next value is called

# the main diff in syntax will be the the use of yield statement

print("==================================================================")


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


print(create_cubes(10))

for x in create_cubes(10):
    print(x)

print("==================================================================")


def create_cubes(n):
    for x in range(n):
        yield x ** 3


for x in create_cubes(10):
    print(x)

print("==================================================================")

print(create_cubes(10))

print("==================================================================")

print(list(create_cubes(10)))

# yield is more memory efficient

print("==================================================================")


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(gen_fibon(10))

print("==================================================================")

for num in gen_fibon(10):
    print(num)

print("==================================================================")


def simple_gen():
    for x in range(3):
        yield x


for x in simple_gen():
    print(x)

print("==================================================================")

gen = simple_gen()

print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

print("==================================================================")

# print(next(gen))
# further the next would give StopIteration Error

# this is also how for loop similarly works internally

# lets try with a string

word = "hello"

for letter in word:
    print(letter)

print("==================================================================")

# but this doesn't means that the string itself is iterating like next(word)

# the following statement will give an TypeError

# print(next(word))

word_iter = iter(word)

print(next(word_iter))
print(next(word_iter))
print(next(word_iter))
print(next(word_iter))
print(next(word_iter))

print("==================================================================")

