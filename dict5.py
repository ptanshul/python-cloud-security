assignments = [
    {
        "properties": {
            "principalId": "111",
            "role": "Reader",
            "environment": "production"
        }
    },
    {
        "properties": {
            "principalId": "222",
            "role": "Owner",
            "environment": "production"
        }
    },
    {
        "properties": {
            "principalId": "333",
            "role": "Owner",
            "environment": "development"
        }
    }
]
for assignment in assignments:
    print(assignment["properties"]["role"])
    
