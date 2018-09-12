import requests
import json


r = requests.get("http://172.16.0.1:8001/FieldData/GetData")
data = r.json()
print(data)





