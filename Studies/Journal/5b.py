# Write a python program to create three dictionaries and concate them to generate a
# new dictionary.

d1, d2, d3 = {1: 2, 3: 4}, {5: 6, 7: 9}, {10: 8, 13: 22}
d4 = {}
for d in [d1, d2, d3]:
    d4.update(d)
print(d4)
