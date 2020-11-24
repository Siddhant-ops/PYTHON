# Write a program to demonstrate json load() and loads() method.

import json

f = open("my_json.json", "r")
print(json.load(f))

content = open("my_json.json", "r")
re = content.read()
print(json.loads(re))
