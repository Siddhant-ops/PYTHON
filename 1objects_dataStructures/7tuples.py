#tuples are similar to lists
#tuples are immutable

t = (1,2,3,4,5,6,7,8);
print(t);

#data type of tuple
print(type(t));

#tuples can contain both strings and numbers
my_tuple = ("one", 2,"three",2,3,4,2,2);
print(my_tuple)

#slicing and indexingcan also be done in tuple

print(my_tuple[0]);
print(t[0:]);
print(t[1:5:2]);

#count() method will count the no. of element in the tuple
print(my_tuple.count(2));

#index() method will show the first index no. of an element
print(my_tuple.index(2));


try:
    # IF YOU WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10;
except:
    print("Hey it looks like u aren't adding correctly");
else:
    print("Yayy u've added successfully")
    print(result);
