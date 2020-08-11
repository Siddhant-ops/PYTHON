print("================================================================================================")

# Regular Expressions Patterns

# Character Identifiers

# Escape Codes
# You can use special escape codes to find specific types of patterns in your data, such as digits, non-digits, whitespace, and more. For example:

# Code	Meaning                                     Example Pattern Code            Example Match
# \d	a digit                                     file_\d\d                       file_25
# \D	a non-digit                                 \D\D\D                          ABC
# \s	whitespace (tab, space, newline, etc.)      a\sb\sc                         a b c
# \S	non-whitespace                              \S\S\S                          Yoyo
# \w	alphanumeric                                \w-\w\w\w                       A-b_1
# \W	non-alphanumeric                            \W\W\W\W\W                      *-+=)
# Escapes are indicated by prefixing the character with a backslash \. Unfortunately, a backslash must itself be escaped in normal Python strings, and that results in expressions that are difficult to read. Using raw strings, created by prefixing the literal value with r, eliminates this problem and maintains readability.

# Personally, I think this use of r to escape a backslash is probably one of the things that block someone who is not familiar with regex in Python from being able to read regex code at first. Hopefully after seeing these examples this syntax will become clear.

import re

text = "My phone number is 1234567890"

phone = re.search(r"1234567890", text)

print(phone)

print("==================================================")

# what if we don't know the phone number but we know it's pattern

text = "My phone number is 1234567890"

# we can use the character identifiers to search for the pattern in search function

phone = re.search(r"\d\d\d\d\d\d\d\d\d\d", text)

print(phone)

print("==================================================")

# Group function shows the actual whole piece of string which is found

print(phone.group())

print("================================================================================================")

# what if we want to search for a pattern of 200 digits, we cannot write '\d' 200 times

# For this reason we can use quantifies for repeating the same character

# Quantifiers

# Character	    Description                                     Example Pattern Code            Example Match

# +	            Occurs oneor more time                          Version \w-\w+                  Version A-b1_1
# {3}           Occurs exactly three times                              \D{3}                           abc
# {2,4}	        Occurs 2 to 4 times                                     \d{2,4}                         123
# {3,}	        Occurs 3 or more times                                  \w{3,}                          anycharacter
# *             Occurs zero or more times                               ABC*                            AAACC
# ?	            Once or none                                            plurals?                        plural

print(re.search(r"\d{10}", text))

print("================================================================================================")

# Let's create a list including 200 characters of '3'

a = "3" * 200

# This will search for 200 charcters of digits

print(re.search(r"\d{200}", a))

print("================================================================================================")

text = "My phone number is 91-1234567890"

print(re.search(r"\d{2}-\d{10}", text))

print("================================================================================================")

# We will now do two task

# 1> to find the phone number

# 2> to extract the area cod that is the '+91'

# we can use groups for any general task that involves grouping together regular expressions and later break them down

# compile function helps in grouping these expressions

# In parenthesis we are gonna group two pattern codes

phone_pattern = re.compile(r"(\d{2})-(\d{10})")

results = re.search(phone_pattern, text)

print(results.group())

print('==================================================')

# now we can also call the groups of the phone pattern individually

# group positions start from 1 and not 0
# group ordering starts at 1

print(results.group(1))

print('==================================================')

print(results.group(2))

# now if i ask for group 3 it'll give me an index Error

