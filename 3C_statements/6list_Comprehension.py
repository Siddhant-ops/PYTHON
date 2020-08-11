# list comprehensions are a quick way of creating lists with python
# if you ever stuck in a situation where you find yourself using a for loop along with a .append() to create a list. List comprehension agreat alternative to that
# for i in range(0, 50):
#   mylist.append(i);
# alternative is List Comprehension


my_string = "hello"

my_list = []

for letter in my_string:
    my_list.append(letter)

print(my_list)

print('================================================================================================')

# alternative to that is List comprehension which is more efficient

my_list = [letter for letter in my_string]

print(my_list)

# new
print('================================================================================================')

new_list = [x for x in "word"]
print(new_list)

print('================================================================================================')

list_1 = [num for num in range(0, 10)]
print(list_1)

# we can also do operations on it

list_2 = [num**2 for num in range(50, 55)]
print(list_2)

# we can also do if statement in list comprehensions

list_3 = [num**2 for num in range(50, 55) if num % 2 == 0]
print(list_3)

# new
print('================================================================================================')

celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celcius]

print(fahrenheit)

fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5) * temp + 32))

print(fahrenheit)

# new
print('================================================================================================')
# trying if/else in List Comprehension

result = [x if x % 2 == 0 else "ODD" for x in range(0, 20)]
print(result)

# in this the odd no.s will get not get printed, instead of them "ODD" will be printed
# [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10, 'ODD', 12, 'ODD', 14, 'ODD', 16, 'ODD', 18, 'ODD']


# new
print('================================================================================================')

# now we will try nested loops in List Comprehensions

mylist = []

for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        mylist.append(x*y)

print(mylist)

# this will multiply x with y and then itwill append it in mylist for every x it will multiply with every y

# we can do this in List Comprehensions in the following way
print('================================================================================================')

ans = [x*y for x in [2, 4, 6] for y in [100, 200, 300]]
print(ans)
