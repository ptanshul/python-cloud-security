import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

data = response.json()

print(data)
print("User ID:", data['userId'])
print("Title:", data['title'])
print ("Completed:", data['completed'])

print(data[0]["title"])  # This line will raise an error because 'data' is a dictionary, not a list.