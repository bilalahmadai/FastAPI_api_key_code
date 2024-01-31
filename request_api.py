import requests

url = "http://127.0.0.1:8000/secure-endpoint"
headers = {"api_key": "bilal123"}
params = {"api_key": "123bilal"}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())
