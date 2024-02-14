import requests
url = 'http://127.0.0.1:8004/getString'
r = requests.get(url)
print(r.json())