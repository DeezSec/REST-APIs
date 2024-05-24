import requests


ask_id = input("which user you would like to update?")
get_id =input("what is the new user name?")
user = {"name": get_id }
headers = {"Content-type": "application/json"}
request = requests.put(f"http://127.0.0.1:8089/users/", json=user, headers=headers)
print(request.json())
print(request.status_code)