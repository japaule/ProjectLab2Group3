## Main file.....
## Project Lab II
## Group Members:
## James Paule
## Jacob Saldua
## Cole Lewis
try:
    from Mqtt import *
    from omnivectors import *
    import json
    from DataClass import *
    import time
    import requests

    mqtt_setup() 		##Set up for mqtt 
    time.sleep(1)   
    sully = 0      ##varible for the solinoid
    ldata = json_data() ##object holds all data from json
    theta = 0
    magnitude = 1
    ldatax = 0
    ldatay = 0
    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
    data = r.json()
    ldata.update(data)

    print("Mqtt setup successful....")
    
    startx = ldata.redcircle_x
    starty = ldata.redcircle_y
    startcx = ldata.redsquare_x;
    startcy = ldata.redsquare_y
##    print("to ball")
##    cordX = ldata.ball_x+10
##    cordY = ldata.ball_y
##    print(ldata.ball_x, " ",ldata.ball_y)
##    last = moverover("r","circle",cordX,cordY, "Rover3", ldata.redcircle_x, ldata.redcircle_y)
##    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##    data = r.json()
##    ldata.update(data)
##    print("touch ball")
##    cordX = ldata.ball_x-2
##    cordY = ldata.ball_y
##    print(ldata.ball_x, " ",ldata.ball_y)
##    last = moverover("r","circle",cordX,cordY, "Rover3", last[0], last[1])
##    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##    data = r.json()
##    ldata.update(data)
##    print("backup")
##    cordX = cordX+5
##    cordY = cordY
##    last = moverover("r","circle",cordX,cordY, "Rover3", last[0], last[1] )
##    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##    data = r.json()
##    ldata.update(data)
##    print("to start")
##    cordX = startx
##    cordY = starty
##    last = moverover("r","circle",cordX,cordY, "Rover3", last[0], last[1])
    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
    data = r.json()
    ldata.update(data)
    print("to ball")
    cordX = ldata.ball_x+7
    cordY = ldata.ball_y
    last = moverover("r","square",cordX,cordY, "Rover2", startcx, startcy)
##    print("touch ball")
##    cordX = ldata.ball_x-10
##    cordY = ldata.ball_y
##    last = moverover("r","circle",cordX,cordY, "Rover1", last[0], last[1])
    print("to goal")
    cordX = 0
    cordY = 50
    last = moverover("r","square",cordX,cordY, "Rover2", last[0], last[1])


finally:
    pubspeeds("Rover1",0,0,0,0)
    pubspeeds("Rover2",0,0,0,0)
    pubspeeds("Rover3",0,0,0,0)
