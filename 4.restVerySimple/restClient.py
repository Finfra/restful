import requests
url = 'http://127.0.0.1:8004/getString'
r = requests.get(url)
data=r.text             #
data=eval(data)         # == data=r.json() 
#print(data["y"])
for i in data:
    print ("%s = %i"%(i,data[i]))
