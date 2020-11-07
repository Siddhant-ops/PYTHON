import json

dict = {"clg": {"faculty": {"name": ["Mrunali", "Riddhi", "Devang", "Prashant"], "roll": [1, 2, 3, 4]}}}

print(json.dumps(dict))

with open("D:\\Main_Folders\\siddhant work\\VS CODE\\PYTHON\\Studies\\PYJSON\\trial1.json", "w") as f:
    json.dump(dict, f)
    print("Dumped!!!")


with open("D:\\Main_Folders\\siddhant work\\VS CODE\\PYTHON\\Studies\\PYJSON\\trial1.json", "r") as f:
    info = json.load(f)
    for i,j,k in info:
        print(info[i])
    print("loaded")
