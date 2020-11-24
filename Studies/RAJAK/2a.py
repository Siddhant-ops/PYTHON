import json

my_file_1=open("my_json.json", "r")
print(json.load(my_file_1))

print("\n================================================\n")

my_file_2=open("my_json.json", "r")
file_read = my_file_2.read()
print(json.loads(file_read))