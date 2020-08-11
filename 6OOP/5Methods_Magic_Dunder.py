print("================================================================================================")

mylist = [1, 2, 3, 4]
print(len(mylist))

# to check the len of the obj

print("================================================================================================")


class Sample:
    pass


# we create an instance of the class
mysample = Sample()

# print(len(mysample))
# we get a error
# TypeError: object of type 'Sample' has no len()

print(mysample)

# here's a way to use the in-built methods such as len, etc on the user-defined objects
# we use special methods/ Magic Methods/ Dunder Methods


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # this is a special method
    # this is equal to str(obj_name)
    def __str__(self):
        return f"{self.title} by {self.author} and has {self.pages} pages"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A Book Class Obj has been deleted")


b = Book("Python Rocks!!!", "Sid", 2000)

# if the __str__ method is not passed
# if it is only written print(b)
# it will give me the output as where this object is located in memory
# <__main__.Book object at 0x000001A37D387488>

print(b)

# __str__
print(str(b))

# __len__
print(len(b))

# this will delete this variable/ obj from the memory of the pc
# __del__
del b

# and hence it won't be able to run this command
print(len(b))
