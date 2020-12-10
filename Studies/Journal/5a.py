# Write a python program to create a dictionary and check whether a particular key is
# present or not.

dict = {1: "hii", 2: "hello", 3: "good", 4: "bye"}


def check_key(key):
    if key in dict.keys():
        print(f"{key} key is one of the keys present in {dict}")
    else:
        print(f"{key} key is not present in this {dict}")


check_key(3)

print("\n==================================================\n")

check_key(6)
