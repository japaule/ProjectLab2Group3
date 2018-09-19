#File used to communicate with esp8266 to gather json location data
# REV 1.1

import time
import serial
import json
import os

print ("CONNECTING......")

ser = serial.Serial('/dev/serial0',115200)
time.sleep(1)
try:
    while True:
##        if ser.inWaiting() > 0:
        rawdata = ser.readline()
##        print("----------------------------------------------------")
        rawdata=rawdata.decode('ASCII')
##            print (rawdata)
        data = json.loads(rawdata)
        os.system('clear')
        print ("Red Circle Center X,Y \t", data["Red Team Data"]["Circle"]["Object Center"]["X"] , " , " ,data["Red Team Data"]["Circle"]["Object Center"]["Y"])
            
        
except KeyboardInterrupt:
    print ("Exiting Program")

##except:
##    print ("Error Occurs, Exiting Program")

finally:
    ser.close()
    pass
