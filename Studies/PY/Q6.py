# Write a python program that creates a tuple,
# t=(19,45,24,60,56,38,21,78,31,5,49,57) and displays all element which
# are less than 50.

t = (19, 45, 24, 60, 56, 38, 21, 78, 31, 5, 49, 57)

print(f"Given tuple : {t}")


print("\n==================================================\n")


new_tuple = tuple(filter(lambda nums: nums < 50, t))

print(f"New tuple with all the values less than 50 : {new_tuple}")
