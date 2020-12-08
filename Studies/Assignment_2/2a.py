# Write a program to demonstrate json load() and loads() method.

import json

s = """{"names": {"siddhant": {"phone_no.": 12345, "roll_no": 0}, "rajak": {"phone_no.": 67890, "roll_no": True}}}"""

mypy = json.loads(s)

with open("D:\\Main_Folders\\siddhant work\\VS CODE\\PYTHON\\Studies\\PYJSON\\trial1.json", "r") as f:
    print(json.load(f))
    print("load")

with open("D:\\Main_Folders\\siddhant work\\VS CODE\\PYTHON\\Studies\\PYJSON\\trial1.json", "r") as content:
    x = content.read()
    print(json.loads(x))
    print("loads")

