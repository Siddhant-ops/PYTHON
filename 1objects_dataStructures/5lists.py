print('\n================================================================================================\n')

# lists are ordered sequences
# they are flexible so they can hold different data types
# list mutable(changable)

# two ways to make a list

# 1st method
list_one = [0] * 3
print(list_one)

print("\n================================================================================================\n")

# 2nd method
list_two = [0, 0, 0]
print(list_two)

print("\n================================================================================================\n")

# example of a list containing numbers
a = [1, 2, 3]
print(a)

print("\n================================================================================================\n")

# example of list containing numbers and string
b = ["hello", "I", "am", "Sid", 18, "years"]
print(b)

print("\n================================================================================================\n")

# len() will return how many elements are present in the list

print(len(a))

print("\n==================================================\n")

print(len(b))

print("\n================================================================================================\n")

# indexing the list
print(a[0])

print("\n================================================================================================\n")

# like strings, list also has slicing and other methods
print(b[1:])

print("\n==================================================\n")

print(b[1:4])

print("\n==================================================\n")

print(b[0:6:1])

print("\n================================================================================================\n")

# concatenation of lists
new_lists = a + b
print(new_lists)

print("\n================================================================================================\n")

# mutation of lists
a[0] = "one"
print(a)

print("\n================================================================================================\n")

# lists methods

# append method adds element to it

a.append("four")
print(a)

print("\n================================================================================================\n")

# pop method will remove element
poped_item = a.pop()
print(poped_item)
print(a)

print("\n================================================================================================\n")

# pop method with indexing
poped_item_2 = a.pop(2)
print(poped_item_2)
print(a)

print("\n================================================================================================\n")

# Normalizing the list the way it was
a.append(3)
print(a)

print("\n================================================================================================\n")

# making a new list for other methods
char_lists = ["a", "s", "e", "u", "r", "w"]
num_lists = [4, 1, 8, 3]

print("\n================================================================================================\n")

# sort method will sort the lists according to alphabets and numbers (A - Z) && (1 - 9)
char_lists.sort()
num_lists.sort()
print(char_lists)

print("\n==================================================\n")

print(num_lists)

print("\n================================================================================================\n")

# sorted lists cannot be stored in other variables it will return nothing and it's data type is none
my_sorted_char_list = char_lists.sort()
print(my_sorted_char_list)

print("\n==================================================\n")

print(type(my_sorted_char_list))

print("\n================================================================================================\n")

# reverse method will reverse everything
num_lists.reverse()
print(num_lists)
