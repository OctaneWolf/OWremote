import requests

url = 'http://localhost:5000/execute'
data = {'command': 'dir'}
response = requests.post(url, json=data)
print(response.json())
