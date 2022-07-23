import requests

BASE = "http://127.0.0.1:5000/"
#headers = {'Content-type': 'application/json; charset=utf-8'}

response = requests.put(BASE + 'video/1', json={"likes" : 10, "name": "dan", "views" : 43}) # PUT Request
print(response.json())
input()
response = requests.get(BASE + 'video/2') # PUT Request
print(response.json())