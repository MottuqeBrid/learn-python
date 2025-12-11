# Requests Module

import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# print(response.json())

data = {"title": "foo", "body": "bar", "userId": 1}

headers = {
    "Content-type": "application/json; charset=UTF-8",
}
res = requests.post(
    "https://jsonplaceholder.typicode.com/todos", headers=headers, json=data
)
print(res.text)
print(res.status_code)
