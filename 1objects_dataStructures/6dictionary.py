print('\n================================================================================================\n')

#dictionaries have keys to represent values
#dictionaries are unordered
#dictionaries are mutable

my_dict = {"key1" : "value1", "key2" : "value2"}
print(my_dict)

print('\n==================================================\n')

print(my_dict["key1"])

print('\n================================================================================================\n')

prices_lookup = {"apple" : 20, "banana" : 30}
print(prices_lookup)

print('\n==================================================\n')

print(prices_lookup["apple"])

print('\n================================================================================================\n')

#nested dictionaries

a = {"k1" : "value1", "k2" : "value2", "k3" : {"kinside1" : "vinside1", "kinside2" : "vinside2"}}
print(a["k3"]["kinside2"])

print('\n================================================================================================\n')

#we can make lists inside dictionaries

b = {"key1" : "v1", "key2" : "v2", "key3" : [0,1,2,"hello",3]}
print(b["key3"][3].upper())

print('\n================================================================================================\n')

#we can add a key value to a dictionay later when it's already initialized

b["key4"] = "v4"
print(b)

print('\n================================================================================================\n')

#dictionary methods

#keys() method will reveal all the keys of the dictionary

print(b.keys())

print('\n================================================================================================\n')

#values() method will show all the values of the dictionary

print(b.values())

print('\n================================================================================================\n')

