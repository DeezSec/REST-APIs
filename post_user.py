import requests

name = input("what would you like to name the user?")
user = {"name": name}
headers = {"Content-type": "application/json"}
request = requests.post("http://127.0.0.1:8089/users", json=user, headers=headers)
print(request.content)
print(request.headers)
print(request.status_code)