import time
import serial
import json

print ("Starting program")

ser = serial.Serial('/dev/serial0',115200)
time.sleep(1)
try:
    while True:
##        if ser.inWaiting() > 0:
        rawdata = ser.readline()
        print("----------------------------------------------------")
        rawdata=rawdata.decode('ASCII')
##            print (rawdata)
        data = json.loads(rawdata)
        
        print(data["Red Team Data"]["Circle"]["Object Center"]["X"])
            
        
except KeyboardInterrupt:
    print ("Exiting Program")

##except:
##    print ("Error Occurs, Exiting Program")

finally:
    ser.close()
    pass
