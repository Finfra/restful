import requests
url = 'http://127.0.0.1:8003/getString'
r = requests.get(url)
print(r.text)
