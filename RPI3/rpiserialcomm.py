#File used to communicate with esp8266 to gather json location data
# REV 1.1

import time
import serial
import json
import os

ser = serial.Serial('/dev/serial0',115200)
time.sleep(1)
try:
    while True:
        rawdata = ser.readline()
        rawdata = rawdata.decode('ASCII')
        data = json.loads(rawdata)
        redcir_x = data["Red Team Data"]["Square"]["Object Center"]["X"]
        redcir_y = data["Red Team Data"]["Square"]["Object Center"]["Y"]
        #---------------------------------
        cor_bl_x = data["Corners"][2]["X"]
        cor_bl_y = data["Corners"][2]["Y"]
        #---------------------------------
        cor_br_x = data["Corners"][3]["X"]
        cor_br_y = data["Corners"][3]["Y"]
        #---------------------------------
        cor_tl_x = data["Corners"][0]["X"]
        cor_tl_y = data["Corners"][0]["Y"]
        #---------------------------------
        cor_tr_x = data["Corners"][1]["X"]
        cor_tr_y = data["Corners"][1]["Y"]
        #---------------------------------
        redcir_x = (256/(cor_tr_x-cor_tl_x)*(redcir_x-cor_tl_x))
        redcir_y = (128/(cor_bl_y-cor_tl_y)*(redcir_y-cor_tl_y))
        print ("x  ",redcir_x)
        print ("y  ",redcir_y)
        #print ("COR_TL \t", cor_tl)
        #print ("Red Circle Center X,Y \t", data["Red Team Data"]["Circle"]["Object Center"]["X"] , " , " ,data["Red Team Data"]["Circle"]["Object Center"]["Y"])
        #print ("X \t",redcir_x,"\n","Y \t",redcir_y)    
        
except KeyboardInterrupt:
    print ("Exiting Program")
#except:
    #print ("Error Occurs, Exiting Program")

finally:
    ser.close()
    pass
