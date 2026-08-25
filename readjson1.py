import json

with open("Audit.json", "r") as file:
    data = json.load(file)

print(data)
