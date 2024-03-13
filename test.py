import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 12000, "name": "Eurovision-Sweden - Markus & Martinus", "views": 473000},
        {"likes": 15000, "name": "Eurovision-Greece - Marina Satti", "views": 1400000},
        {"likes": 11000, "name": "Eurovision-Croatia - Baby lasagna", "views": 402000},
        {"likes": 36000, "name": "Eurovision-Irland - Bambie thug", "views": 302000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())
