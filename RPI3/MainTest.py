## Main file.....
## Project Lab II
## Group Members:
## James Paule
## Jacob Saldua
## Cole Lewis

from pix2coord import *
from Mqtt import *
from omnivectors import *
from rpiserialcomm import *
import serial
import json
from DataClass import *

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
   		print(ldata.ball_x," ",ldata.ball_y)
        #a = updatejson(ser)
        #time.sleep(2)
        #if ((abs(bluecircle.x-redcircle.x))<15 and abs((bluecircle.y-redcircle.y)<15)):
         #   sully = 1
        #else:
         #   sully = 0
        #print("redsquare")
        # redsquare.printobj()
        #print("redcircle")
       # a.printobj()
    
        #change = move(a.x,a.y,100,50)
    except:
        print("Houston We Have A Problem")

    # magnitude = math.sqrt((change[0]*change[0])+(change[1]*change[1]))
    # print(change)

    # if(magnitude != 0):
    #     changeX=(change[0]/magnitude)*300
    #     changeY=(change[1]/magnitude)*300

    #     b = vectors(0,changeX,-changeY,0)
    #     print("motor speeds")
    #     print(b)
    #     pubspeeds("Rover1",b[0],b[1],b[2],sully)
    #     #time.sleep(1)
    #     pubspeeds("Rover1",0,0,0,sully)
    # else:
    #     pubspeeds("Rover1",0,0,0,sully)

    # ser.close()
    #time.sleep(1)
    # ser = serial.Serial('/dev/serial0',115200) ##declare ser object for serial comms
    #--------------------------------------------------------------------------------------------------------------------------------------
    
