import requests

BASE = "http://127.0.0.1:5000/"
#headers = {'Content-type': 'application/json'}

response = requests.get(BASE) # PUT Request
print(response.json())