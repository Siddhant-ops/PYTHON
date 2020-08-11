# ========================================================================
# Write a function that computes the volume
# of a sphere given its radius.

# The volume of a sphere is given as (( 4 * π * (r*r*r) ) / 3 )

import string

print("================================================================================================")

print("Volume of a sphere")


def vol(rad):
    result = (4 * 3.14 * (rad ** 3)) / 3
    return result


print(vol(2))

# ========================================================================

# Write a function that checks
# whether a number is in a given range (inclusive of high and low)

print("================================================================================================")

print("ran_check")


def ran_check(high, low, num):
    if num in range(low, high + 1):
        print("{} is in range of {} and {}".format(num, high, low))
    else:
        print("{} is not in range of {} and {}".format(num, high, low))


print(ran_check(20, 5, 32))

print("================================================================================================")

# If you only wanted to return a boolean:


def ran_bool(high, num, low):
    return num in range(low, high + 1)


print(ran_bool(50, 58, 60))

print("================================================================================================")

# ========================================================================

# Write a Python function
# that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: .isupper() and .islower()
# If you feel ambitious, explore the Collections module to solve this problem!

print("New")
print("Up_low")

print("================================================================================================")


def up_low(mystring):

    up_lets = 0
    low_lets = 0
    extra_objects = 0

    for letters in mystring:
        if letters.isupper():
            up_lets += 1
        elif letters.islower():
            low_lets += 1
        else:
            extra_objects += 1

    print(up_lets)
    print(low_lets)
    print(extra_objects)


print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))

print("================================================================================================")

# ========================================================================

# Write a Python function that
# takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

print("unique_list")


def unique_list(lst):
    x = []
    for things in lst:
        if things not in x:
            x.append(things)
    return x


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

print("================================================================================================")

# ========================================================================

# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]

# Expected Output : -24

print("Multiply")


def multiply(numbers):
    a = 1
    for i in numbers:
        a *= i
    return a


print(multiply([1, 2, 3, -4]))

print("================================================================================================")

# ========================================================================

# Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
# e.g., madam or nurses run

print("palindrome")


def palindrome(s):
    s = s.replace(" ", "")
    reverse = s[::-1]
    return s == reverse


print(palindrome("sid"))
print(palindrome("helleh"))
print(palindrome("nurses run"))
print(palindrome("madam"))
print(palindrome("abcba"))

print("================================================================================================")

# ========================================================================

# Hard:

# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

# For example : "The quick brown fox jumps over the lazy dog"

# Hint: Look at the string module

print("================================================================================================")

print("ispanagram")


def ispanagram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print(alphaset)
    return alphaset <= set(str1.lower())


print(ispanagram("The quick brown fox jumps over the lazy dog"))

# ========================================================================
