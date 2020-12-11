# Write a function that accepts only single character and returns true if it is a vowel.


def check_vowel(a):
    if a.isalpha() and len(a) == 1:
        if a.lower() == "a" or a.lower() == "e" or a.lower() == "i" or a.lower() == "o" or a.lower() == "u":
            return True


print(check_vowel("z"))
print(check_vowel("A"))
