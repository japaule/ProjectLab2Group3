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

<<<<<<< HEAD
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
=======
#from pix2coord import *
from Mqtt import *
from omnivectors import *
#from rpiserialcomm import *
import serial
import json
from DataClass import *
import time

print("Serial Comm setup...")
#
ser = serial.Serial('/dev/serial0',115200) ##declare ser object for serial comms
time.sleep(1)
mqtt_setup() 							##Set up for mqtt 
time.sleep(1)
sully = 0
ldata = json_data()




print("Application Starting.....")


##-----------------------------------------------------------

##------------------------------------------------------------

while True:
    
    time.sleep(.555)
##    pubspeeds("Rover2",0,0,0,sully)
    try:
        if ser.inWaiting() > 0:
            rawdata = ser.readline()
            rawdata = rawdata.decode('ASCII')
            data = json.loads(rawdata)
            ldata.update(data)
            #time.sleep(2)
        if ((abs(ldata.bluecircle_x-ldata.redcircle_x))<15 and abs((ldata.bluecircle_y-ldata.redcircle_y)<15)):
            sully = 1
        else:
            sully = 0

        change = move(ldata.bluesquare_x,ldata.bluesquare_y,100,50)

        magnitude = math.sqrt((change[0]*change[0])+(change[1]*change[1]))
        # print(change)

        if(magnitude != 0):
            changeX=(change[0]/magnitude)*300
            changeY=(change[1]/magnitude)*300
>>>>>>> 5e87f194f2bbe21edf1961c00226e3fc689fb17d

            b = vectors(0,changeX,-changeY,0)
            print("motor speeds")
        #     print(b)
            pubspeeds("Rover1",b[0],b[1],b[2],sully)
            time.sleep(1)
            pubspeeds("Rover1",0,0,0,sully)
        else:
            pubspeeds("Rover1",0,0,0,sully)
    except:
        	#print("Houston We Have A Problem")

<<<<<<< HEAD
finally:
    pubspeeds("Rover1",0,0,0,0)
    pubspeeds("Rover2",0,0,0,0)
    pubspeeds("Rover3",0,0,0,0)
=======
       
    #--------------------------------------------------------------------------------------------------------------------------------------
    
>>>>>>> 5e87f194f2bbe21edf1961c00226e3fc689fb17d
