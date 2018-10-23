## This application is designed to ping and parse data from TTUSwarmField in json format.
## Additonally, it converts the pixel data to coordinates
## Project Lab II
## Group Members:
## James Paule
## Jacob Saldua
## Cole Lewis


from rpiserialcomm import *
from pix2coord import *
from Mqtt import *

sully = 0

print("Application Starting.....")

##Serial Comm Setup
print("Serial Comm setup...")
ser = serial.Serial('/dev/serial0',115200)
time.sleep(1)
mqtt_setup()
time.sleep(1)

##updatejson(ser)
while True:
        updatejson(ser)
        time.sleep(.25)
        pubspeeds("Rover1",100,-200,100,sully)
        if ((abs(ball.x-redcircle.x))<5 && abs((ball.y-redcircle.y)<5)):
                sully = 1
        else:
                sully = 0
    
    
        #ser.close()
        
        
    
