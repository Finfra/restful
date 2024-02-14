import requests

url = 'http://127.0.0.1:8006/users/1'
r = requests.get(url)
print(url ," →  return = ", r.text)

url = 'http://127.0.0.1:8006/users/2'
r = requests.get(url)
print(url ," →  return = ", r.text)
