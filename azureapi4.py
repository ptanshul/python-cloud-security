import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

data = response.json()

print(data)
for todo in data:
    if not todo['completed']:
        print("Incomplete task:")
        print("User ID:", todo['userId'])
        print("Title:", todo['title'])
