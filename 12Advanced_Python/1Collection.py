from collections import defaultdict
from collections import Counter

print("==================================================================")

# Collection module implements specialized container data types that are essentially alternatives


# so now we have imported Counter method from collection modules

# Counter method counts how many unique elements are passed, how many times in the list/ string/ tuple, and Counter returns them as a dictionary

mylist = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

count_mylist = Counter(mylist)

print(count_mylist)

print("==================================================================")


mylist = ["a", "a", "a", "a", 10, 10, 10, 10, 10]

c_list = Counter(mylist)

print(c_list)

print("\n================================================================================================\n")

print(Counter("aassdfugaggidugai"))

print("\n================================================================================================\n")

sentence = "How many times does each word shows up in this sentence with a word"

sentence = sentence.lower().split()

print(Counter(sentence))

print("\n================================================================================================\n")

print("\n================================================================================================\n")

# Common patterns when using the Counter() object
#
#
# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts

print(list(Counter(mylist)))

print("\n================================================================================================\n")

# now we will explore default dict


d = {"a": 10}

print(d)

print("\n================================================================================================\n")

print(d["a"])

print("\n================================================================================================\n")

# now we will call a wrong key which has not been passed in the 'd' dictionary and it will give a keyerror

# print(d["wrong"])

# now we will create a defaultdict, now it's job is that if we call a wrong key, it will assign a value to it and make it a key of that dictionary

d = defaultdict(lambda: 0)

print("\n================================================================================================\n")

# now we make a new key for dictionary and declare it's value 100

d["correct"] = 100

print(d["correct"])

print("\n================================================================================================\n")

# now we will print a key of the dictionary which has not yet been declared yet

# but because of the defaultdic from collection module it will assign a value 0

print(d["wrong"])

print("\n================================================================================================\n")

# Now we will explore the namedtuple method of collection module

# we will create a simple tuple

mytuple = (10, 20, 30)

# now let's grab an element from the tuple

print(mytuple[0])

print("\n================================================================================================\n")

# now since the tuple is small it's easy to grab an element

#  What if the tuple would had been large, then the question would arise, how to grab the element of big tuple

# there's a way to solve that issue with namedtuple

from collections import namedtuple

Dog = namedtuple("dog", ["age", "breed", "name"])

print(Dog)

print("\n==================================================\n")

sammy = Dog(age=5, breed="husky", name="sam")

print(sammy)

print("\n==================================================\n")

rex = Dog(10, "german", "rex")

print(rex)

print("\n==================================================\n")

print(sammy.age)

print("\n==================================================\n")

print(rex.breed)

print("\n==================================================\n")

print(sammy.name)

print("\n==================================================\n")

print(rex[1])

