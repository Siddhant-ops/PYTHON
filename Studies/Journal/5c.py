# Write a python program to sum all the elements of the dictionary.

my_dict = {1: 15, 2: "hello", 3: 11, 4: "my", 5: 12, 6: "name", 7: 13, 8: "is", 9: 14, 10: "X"}


def sum_dict(dictionary):
    sum = 0
    for i in my_dict:
        if isinstance(my_dict[i], int):
            sum += my_dict[i]
    print(sum)


sum_dict(my_dict)
