print("================================================================================================")

# We already know we can search for substring within a larger string with the in opearor

# eg: return 'dog' in 'My dog is my friend'

# But this has severe limitations, we need to know the exact string, and need to perform additional opartions to account for capitalization and punctuation.

# What if we only want to search for a pattern structure of the string we are looking for

# Regular Expressions (regex) allow usto search for general patterns in text data!

# eg a simple email format can be - user@email.com

# We know in this case we are looking for a pattern "text" + "@" + "text" + ".com"

# Pyhton comes with a builtin regular expressions library 're' for short. It allows us to create specialized pattern strings and then search for matches within text

# The primary skillset for regex is undrstanding the special syntax for these pattern strings.

# eg for a phone number let's say my number +91-1234567890

# in regex pattern - r"+(\d\d)-(\d\d\d\d\d\d\d\d\d\d)

# or

# in regex pattern - r"+(\d{2})-(\d{10})

# \d stands for digits

# let's start with re library

text = "The agent's phone number is +91-1234567890. Call soon!"

print("phone" in text)

print("================================================================================================")

# now let's import re library

import re

# we will assign "phone" string to a variable

pattern = "phone"

# search function takes 2 args (what to search, where to search)

print(re.search(pattern, text))

# It returns the result in an object and also return where in the string the object is

print("==================================================")

re_search = re.search(pattern, text)

# we can call the span method to locate at which the string is stored at

print(re_search.span())

print("==================================================")

# start method will display the starting index of the search_string

print(re_search.start())

print("================================================================================================")

# end method will display the ending index of the search_string

print(re_search.end())

print("================================================================================================")

# the search function only shows the first appearance of the search_string

# currently the string in which we want to test is :

text = "The agent's phone number is +91-1234567890. Call soon!"

# Let's now trick it and make a string in which the word 'phone' has appeared twice :

text = "my phone once, my phone twice"

# Now let's use search function and see the output

match = re.search("phone", text)

print(match)

print("==================================================")

# to find all the matches in the text string we can use findall function to return a list of search_string

matches = re.findall("phone", text)

print(matches)

print("==================================================")

print(len(matches))

print("==================================================")

# we can use the finditer function to iter our search_string which would reveals all the starting and ending indexes

for mat in re.finditer("phone", text):
    print(mat)
