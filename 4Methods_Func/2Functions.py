# functions allow us to create blocks of code that can be easily executed many times,
# without needing to constantly rewrite the entire block of code

# syntax of function


def name_of_function():
    """Docstring explains function."""
    print("Hello")


def name_of_function(name):
    """Docstring explains function."""
    print("Hello " + name)


# in the following function adding_two_no we are gonna take two parameters a & b and the function will return a + b. function calling is assigned to a variable result and we would print(result) and pass parameters to the function while calling and assigning it to the variable.


def adding_two_no(a, b):
    return a + b


result = adding_two_no(5, 3)

print(result)

# new
print("================================================================================================")


def dog_check(my_string):
    return "dog" in my_string.lower()


print(dog_check("the name of my Dog is Max"))

# new
print("================================================================================================")

# PIG LATIN
# if a word starts with a vowel, add 'ay' to end
# if a word does not start with a vowel, put the first letter at the end, then add 'ay'
# word -> ordway
# apple -> appleay

# making a pig latin translator function


def pig_latin(word):
    first_letter = word[0]
    if first_letter.lower() in "aeiou":
        return word + "ay"
    else:
        return word[1:] + first_letter + "ay"


result = pig_latin("escape")
ans = pig_latin("word")
print(ans)
print(result)
