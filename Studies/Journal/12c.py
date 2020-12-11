import json

json_obj = '{"Name":"Sid", "Class":"SY", "Course":"BSCIT", "Age":18}'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)

print("\nPython object:")
print("Name: ", python_obj["Name"])
print("Class: ", python_obj["Class"])
print("Course: ", python_obj["Course"])
print("Age: ", python_obj["Age"])


print("\n==================================================\n")

python_obj = {"Name": "Sid", "Class": "SY", "Course": "BSCIT", "age": 18}
print("Python object:")
print(type(python_obj))
print(python_obj)

print("\nJSON data:")
j_data = json.dumps(python_obj)
print(j_data)
