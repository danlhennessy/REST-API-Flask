import requests

BASE = "http://127.0.0.1:5000/"
#headers = {'Content-type': 'application/json; charset=utf-8'}

response = requests.put(BASE + 'video/1', json={"likes" : 10}) # PUT Request
print(response.json())