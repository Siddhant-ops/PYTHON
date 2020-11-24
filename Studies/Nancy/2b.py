# Write a program to demonstrate json dump and dumps() method.

import json

my_dict = {"names": {"Nancy": {"roll_no.": 123, "div": 1}, "Khanak": {"roll_no..": 678, "div": 4}}}

myjson = json.dumps(my_dict)
print(myjson)

f = open("new_json_2b_py.json", "w")
json.dump(my_dict, f)
