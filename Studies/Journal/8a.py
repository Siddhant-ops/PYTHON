# Create a string in python with minimum length of 3 characters and perform the
# following operations:
# a) Add 'ing' at the end of a string
# b) If string already ends with 'ing' then add 'ly' at the end of the string
# c) Perform nothing if length of a string is less than 3


def condition_string(my_string):
    len_my_string = len(my_string)
    if len_my_string > 2:
        if my_string[-3:] == "ing":
            new_string = my_string + "ly"
        else:
            new_string = my_string + "ing"
        print(new_string)
    else:
        pass


word_list = ["understanding", "partner", "as", "perfect", "young", "parking", "by"]

for i in word_list:
    condition_string(i)
