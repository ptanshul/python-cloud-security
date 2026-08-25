import json

with open("Audit.json", "r") as file:
    data = json.load(file)

for event in data:
    print(event.keys())