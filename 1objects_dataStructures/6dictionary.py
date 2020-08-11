#dictionaries have keys to represent values
#dictionaries are unordered
#dictionaries are mutable

my_dict = {"key1" : "value1", "key2" : "value2"};
print(my_dict);

print(my_dict["key1"]);

prices_lookup = {"apple" : 20, "banana" : 30};
print(prices_lookup);
print(prices_lookup["apple"]);

#nested dictionaries

a = {"k1" : "value1", "k2" : "value2", "k3" : {"kinside1" : "vinside1", "kinside2" : "vinside2"}};
print(a["k3"]["kinside2"]);

#we can make lists inside dictionaries

b = {"key1" : "v1", "key2" : "v2", "key3" : [0,1,2,"hello",3]};
print(b["key3"][3].upper());

#we can add a key value to a dictionay later when it's already initialized

b["key4"] = "v4";
print(b);

#dictionary methods

#keys() method will reveal all the keys of the dictionary

print(b.keys());

#values() method will show all the values of the dictionary

print(b.values());

