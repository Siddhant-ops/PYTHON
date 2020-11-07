print("\n================================================================================================\n")

import re

# now we will use or operator in searching two different patterns to search in a given text

print(re.search(r"cat|dog", "I love dogs!"))

print("\n==================================================\n")

print(re.search(r"cat|dog", "I love cats!"))

print("\n================================================================================================\n")

# A wildcard operator is '.'
# the wildcard reveals 'x' number of character when 'x' times the wildcard operator is inserted

print(re.findall(".at", "the cat in the hat sat there"))

print("\n==================================================\n")

print(re.findall("...at", "the cat in the hat went splat"))

print("\n================================================================================================\n")

# let's discuss wildcard starts with

# '^' this searches if the regex expression is located at the start of the string

print(re.findall(r"^\d", "1 is one"))

print("\n==================================================\n")

# note : it won't return anyhting coz the digit isn't in starting of the string

print(re.findall(r"^\d", "the 1 is one"))

print("\n==================================================\n")

# let's discuss wildcard end with

# '$' this searches if the regex expression is located at the end of the string

print(re.findall(r"\d$", "Two is 2"))

print("\n==================================================\n")

# note : it won't return anyhting coz the digit isn't in ending of the string

print(re.findall(r"\d$", "two is 2 not one"))

print("\n================================================================================================\n")

# if you want to exclude (removes) any part

phrase = "there are 3 numbers 34 inside 5 this sentence"

pattern = r"[^\d]+"
# this excludes only digits

print(re.findall(pattern, phrase))

print("\n==================================================\n")

test_phrase = "this is a string! But it has punctuation. How can we remove it?"

clean = re.findall(r"[^!.? ]+", test_phrase)

# In clean : !.? and ' ' is gonna be removed

# in order to join them we can use " ".join(clean) to join the list

print(" ".join(clean))

print("\n================================================================================================\n")

# Now let's find the hypen words.

text = "only find the hypen-words in this sentence. But you do not know how long-ish is this"

# [\w]+ this says a group of alphanumeric characters

# but hypen words are two words with '-' this sign in middle.
# [\w]+-[\w]+

pattern = r"[\w]+-[\w]+"

print(re.findall(pattern, text))

print("\n================================================================================================\n")

text = "Hello, would you like some catfish?"
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

text_list = [text, texttwo, textthree]

print(text_list)

print("\n==================================================\n")

for my in text_list:
    print(re.search(r"cat(fish|nap|erpillar)", my))
    print("\n==================================================\n")

