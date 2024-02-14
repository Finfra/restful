import requests
data = dict(name="Joe", comment="A test comment")
r = requests.post("http://127.0.0.1:8007/post", data=data)
print(r.json())