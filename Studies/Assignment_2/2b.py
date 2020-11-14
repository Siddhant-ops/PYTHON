# Write a program to demonstrate json dump and dumps() method.

import json

mydict = {"names": {"siddhant": {"phone_no.": 12345, "roll_no": 00}, "rajak": {"phone_no.": 67890, "roll_no": 10}}}

obj_json = json.dumps(mydict)
print(obj_json)
print("dumps")

with open("new_json_2b_py.json", "w") as f:
    json.dump(mydict, f)
print("dump")