# Write a program to demonstrate json dump and dumps() method.

import json

my_dict = { 'dictA': {'key_1': 'value_1'},'dictB': {'key_2': 'value_2'}}

obj_json=json.dumps(my_dict)
print(obj_json)

with open("new_json_2b_py.json", "w") as f:
    json.dump(my_dict, f)