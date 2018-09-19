import requests
import json

while True:
    try:
        r = requests.get("http://172.16.0.1:8001/FieldData/GetData")
        data = r.json()
        print(data["Red Team Data"]["Circle"]["Object Center"]["X"])
    except:
        print("Error")





