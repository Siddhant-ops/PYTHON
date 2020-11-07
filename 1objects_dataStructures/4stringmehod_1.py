print("\n================================================================================================\n")

# .format() is a method which will insert the given parameters into the string to which it is applied

print("This is a string {}".format("Inserted"))

print("\n==================================================\n")

# it is also used to insert multiple parameters

print("The {} {} {} ".format("fox", "brown", "quick"))

print("\n==================================================\n")

# In the .format() method the parameters are given index no. respectively and can be used in the string inside the block codes

print("The {2} {1} {0} ".format("fox", "brown", "quick"))

print("\n==================================================\n")

# we can also give keys to the parameters (preferrable to remember)

print("The {c} {b} {a} ".format(a="fox", b="brown", c="quick"))

print("\n==================================================\n")

# we can use it to store any mathematical values and use it in print()

result = 26966 / 56

print("The result is {r}".format(r=result))

print("\n==================================================\n")

# we can use it to declare how much the width of the parameter should be

result = 26966 / 56

print("The result is {r:1.3f}".format(r=result))

print("\n==================================================\n")

# Fstrings or formatted strings

name = "Sid"

print(f"Hello {name}, welcome back")

print("\n==================================================\n")

age = 18

print(f"{name} is {age} years old")

print("\n==================================================\n")

