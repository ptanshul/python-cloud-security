import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

data = response.json()

print(data)
for todo in data:
    print("User ID:", todo['userId'])
    print("Title:", todo['title'])
    print("Completed:", todo['completed'])
