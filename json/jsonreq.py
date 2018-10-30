import requests
import json

while True:
    try:
        r = requests.get("http://172.16.0.1:8001/FieldData/GetData")
        data = r.json()
        print(data["Blue Team Data"]["Square"]["Object Center"]["X"])
        print("\033[H\033[J")
    except:
        print("Error")





