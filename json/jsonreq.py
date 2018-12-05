import requests
import json
import time

while True:
    time.sleep(.1)
    try:
        r = requests.get("http://172.16.0.1:8001/FieldData/GetData")
        data = r.json()
        print(data["Red Team Data"]["Circle"]["Object Center"]["X"])
    except:
        print("Error")





