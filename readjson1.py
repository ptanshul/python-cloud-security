import json

with open("Audit.json", "r") as file:
    data = json.load(file)

event = data[0]

for key in event:
    print(key)