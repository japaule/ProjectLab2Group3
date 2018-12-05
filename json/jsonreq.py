import requests
import json
import time

while True:
    time.sleep(.1)
    try:
        r = requests.get("http://172.16.0.1:8001/FieldData/GetData")
        data = r.json()
        print(data["Blue Team Data"]["Square"]["Object Center"]["X"])
        print("\033[H\033[J")
    except:
        print("Error")





