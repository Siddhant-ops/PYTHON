# Write a program to demonstrate json load() and loads() method.

import json

fil=open("my_json.json", "r")
print(json.load(fil))

cont=open("my_json.json", "r")
st = cont.read()
print(json.loads(st))