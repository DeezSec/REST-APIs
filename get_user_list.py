import requests

request = requests.get("http://127.0.0.1:8089/user_list")
print(request.json())
print(request.status_code)