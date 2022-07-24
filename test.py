import requests

BASE = "http://127.0.0.1:5000/"

data= [{"likes" : 14, "name": "tony", "views" : 43},
       {"likes" : 10, "name": "dan", "views" : 12},
       {"likes" : 1000, "name": "scell", "views" : 4332}
       ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())