import requests
url = 'http://127.0.0.1:8005/getString'
r = requests.get(url)
data=r.json()
#print(data["y"])
for i in data:
    print ("%s = %i"%(i,data[i]))

url = 'http://127.0.0.1:8004/users/aa'
r = requests.get(url)
print(url ," →  return = ", r.text)

url = 'http://127.0.0.1:8004/users/xx'
r = requests.get(url)
print(url ," →  return = ", r.text)
