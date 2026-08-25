import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

data = response.json()

print(data)
print("User ID:", data[0]['userId'])
print("Title:", data[0]['title'])
print("Completed:", data[0]['completed'])