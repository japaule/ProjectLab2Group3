## Main file.....
## Project Lab II
## Group Members:
## James Paule
## Jacob Saldua
## Cole Lewis

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
    
    time.sleep(.25)
##    pubspeeds("Rover2",0,0,0,sully)
    try:
        for x in range(0, 10):
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
        #print(data["Blue Team Data"]["Square"]["Object Center"]["X"])
        #print(ldata.bluecircle_x," ", ldata.bluecircle_y)
        #print(ldata.redcircle_x," ", ldata.redcircle_y)
        #last = ldata
        #change = move(ldata.bluesquare_x,ldata.bluesquare_y,last.bluesquare_x,last.bluesquare_y)
        print(ldata.ball_x," ", ldata.ball_y)  
        print(ldata.bluesquare_x," ", ldata.bluesquare_y)
        change = move(ldata.bluesquare_x,ldata.bluesquare_y,ldata.ball_x,ldata.ball_y)

        magnitude = math.sqrt((change[0]*change[0])+(change[1]*change[1]))
        # print(change)

        if(magnitude != 0):
            changeX=(change[0]/magnitude)*600
            changeY=(change[1]/magnitude)*600

            b = vectors(0,changeX,-changeY,0)
            #print("motor speeds")
            print(b)
            pubspeeds("Rover1",int(b[0]),int(b[1]),int(b[2]),sully)
            t=(magnitude/223) *10
            time.sleep(t)
            #print(t)
            #print(magnitude)
            pubspeeds("Rover1",0,0,0,sully)
        else:
            pubspeeds("Rover1",0,0,0,sully)
    except:
        	print("Houston We Have A Problem")

       
    #--------------------------------------------------------------------------------------------------------------------------------------
    
