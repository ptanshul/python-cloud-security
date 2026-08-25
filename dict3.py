assignments = [
    {
        "user": "alice",
        "role": "Reader"
    },
    {
        "user": "bob",
        "role": "Contributor"
    },
    {
        "user": "charlie",
        "role": "Owner"
    }
]

dangerous_roles = ["Owner", "User Access Administrator"]
for assignment in assignments:
    print(assignment)
for assignment in assignments:
    print(f"User: {assignment['user']}, Role: {assignment['role']}")

for assignment in assignments:
    if assignment["role"] in dangerous_roles:
        print(f"Security Alert !! User {assignment['user']} has a dangerous role: {assignment['role']}.")