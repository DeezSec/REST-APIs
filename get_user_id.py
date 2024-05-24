import requests

id = input("which employee id would you like to see? [available IDs are 000, 001, 002, 003]:")
request = requests.get(f'http://127.0.0.1:8089/user_id')
print(request.json())
print(request.status_code)