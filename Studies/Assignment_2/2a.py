# Write a program to demonstrate json load() and loads() method.

import json

with open("D:\\Main_Folders\\siddhant work\\VS CODE\\PYTHON\\Studies\\PYJSON\\trial1.json", "r") as f:
    print(json.load(f))
    print("load")

with open("D:\\Main_Folders\\siddhant work\\VS CODE\\PYTHON\\Studies\\PYJSON\\trial1.json", "r") as content:
    x = content.read()
    print(json.loads(x))
    print("loads")
