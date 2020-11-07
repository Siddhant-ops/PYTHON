print("\n================================================================================================\n")

# Execute various functions of list and display output.

mylist = [412, 142, 1103, 1423462, 1103, 673, 34532, 863452, 1103, 428893, 8198126]
print(mylist)


print("\n==================================================\n")


# sort(): Sorts the list in ascending order.

mylist.sort()
print(f"Sorted List : {mylist}")


print("\n==================================================\n")


# append(): Adds a single element to a list.

mylist.append("Python")
print(f"Append method : {mylist}")


print("\n==================================================\n")


# extend(): Adds multiple elements to a list via an iterative object

temp_list = ["is", "COOL"]

mylist.extend(temp_list)
print(f"Extended List : {mylist}")


print("\n==================================================\n")


# index(): Returns the first appearance of the specified value.

print(f"Index method : {mylist.index(1103)}")


print("\n==================================================\n")


# max(list): It returns an item from the list with max value.

only_ints = [412, 142, 1103, 1423462, 1103, 673, 34532, 863452, 428893, 8198126]
print(f"Max method : {max(only_ints)}")


print("\n==================================================\n")


# min(list): It returns an item from the list with min value.


only_ints = [412, 142, 1103, 1423462, 1103, 673, 34532, 863452, 428893, 8198126]
print(f"Min method : {min(only_ints)}")


print("\n==================================================\n")


# len(list): It gives the total length of the list.

print(f"Length of the list : {len(mylist)}")


print("\n==================================================\n")


# list(seq): Converts a tuple into a list.

new_lists = list(range(0, 101, 5))
print(f"Converting a sequence into list : {new_lists}")


print("\n==================================================\n")


# pop(index): pop method will remove the particular element present at the given index

mylist.pop(4)
print(f"Poping an elemennt : {mylist}")


print("\n==================================================\n")


# insert(index, object): insert method will push an object into the sequence at the given index

mylist.insert(-1, "very")
print(f"Insert method : {mylist}")


print("\n==================================================\n")


# copy(): copy method will return the copy of the list

my_list = mylist.copy()
print(f"Copy method : {my_list}")


print("\n==================================================\n")


# count(object): count method will count the number of times the object is present in the sequence

print(f"Count method : {mylist.count(1103)}")


print("\n==================================================\n")


# reverse(): reverse method will return the reverse version the llist

mylist.reverse()
print(f"Reverse method : {mylist}")


print("\n==================================================\n")


# remove() : remove method will remove the first occurence of the list

mylist.remove(1103)
print(f"Remove method : {mylist}")


print('\n==================================================\n')

# clear(): clear method will remove all the elements from the list

my_list.clear()
print(f"Clear method : {my_list}")
