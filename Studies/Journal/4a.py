# Write a function that accepts only single character and returns true if it is a vowel.


def check_vowel(a):
    if a.isalpha() and len(a) == 1:
        if a.lower() == "a" or a.lower() == "e" or a.lower() == "i" or a.lower() == "o" or a.lower() == "u":
            print(f"{a} is a vowel")
        else:
            print(f"{a} is not a vowel")
    else:
        print("You did not enter a single character")


check_vowel("A")
