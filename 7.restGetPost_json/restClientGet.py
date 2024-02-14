import requests
url = 'http://127.0.0.1:8007/get'
r = requests.get(url)
print(r.json())