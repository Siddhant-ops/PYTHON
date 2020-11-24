import json

dict = {
    "Laptop": {"sony": 1, "apple": 2, "asus": 5},
    "Camera": {"sony": 2, "sumsung": 1, "nikon": 4},
}

myjson = json.dumps(dict)
print(myjson)

with open("new_json_py.json", "w") as my_f:
    json.dump(dict, my_f)

