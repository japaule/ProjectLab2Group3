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

print("Serial Comm setup...")
#
ser = serial.Serial('/dev/serial0',115200) ##declare ser object for serial comms
time.sleep(1)
mqtt_setup() 							##Set up for mqtt 
time.sleep(1)
#ser = serial.Serial('/dev/serial0',115200) ##declare ser object for serial comms

sully = 0

##if ser.inWaiting() > 0:
##    rawdata = ser.readline()
##    rawdata = rawdata.decode('ASCII')
##    data = json.loads(rawdata)
##    #print(data)
##    
##    
##    cor_br = corners(data["Corners"][2]["X"],data["Corners"][2]["Y"])
##    cor_tr = corners(data["Corners"][3]["X"],data["Corners"][3]["Y"])
##    cor_bl = corners(data["Corners"][0]["X"],data["Corners"][0]["Y"])
##    cor_tl = corners(data["Corners"][1]["X"],data["Corners"][1]["Y"])
##    cval = maxmin_xy(cor_tl.x, cor_tr.x, cor_bl.x, cor_br.x, cor_tl.y, cor_tr.y, cor_bl.y, cor_br.y) #find the max and min values of the corners 
##    
##    redcircle = objpos(data["Red Team Data"]["Circle"]["Object Center"]["X"],data["Red Team Data"]["Circle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##    redsquare = objpos(data["Red Team Data"]["Square"]["Object Center"]["X"],data["Red Team Data"]["Square"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##    redtriangle = objpos(data["Red Team Data"]["Triangle"]["Object Center"]["X"],data["Red Team Data"]["Triangle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##    
##    bluecircle = objpos(data["Blue Team Data"]["Circle"]["Object Center"]["X"],data["Blue Team Data"]["Circle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##    bluesquare = objpos(data["Blue Team Data"]["Square"]["Object Center"]["X"],data["Blue Team Data"]["Square"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##    bluetriangle = objpos(data["Blue Team Data"]["Triangle"]["Object Center"]["X"],data["Blue Team Data"]["Triangle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##    
##    ball = objpos(data["Ball"]["Object Center"]["X"],data["Ball"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)





##def updatejson(ser):	
##    if ser.inWaiting() > 0:
##        rawdata = ser.readline()
##        rawdata = rawdata.decode('ASCII')
##        data = json.loads(rawdata)
##        print("blue square")
##        print(data["Blue Team Data"]["Square"]["Object Center"]["X"])
##        #print(data)
##        
##       
##        cor_br = corners(data["Corners"][2]["X"],data["Corners"][2]["Y"])
##        cor_tr = corners(data["Corners"][3]["X"],data["Corners"][3]["Y"])
##        cor_bl = corners(data["Corners"][0]["X"],data["Corners"][0]["Y"])
##        cor_tl = corners(data["Corners"][1]["X"],data["Corners"][1]["Y"])
##        cval = maxmin_xy(cor_tl.x, cor_tr.x, cor_bl.x, cor_br.x, cor_tl.y, cor_tr.y, cor_bl.y, cor_br.y) #find the max and min values of the corners 
##        
##        redcircle = objpos(data["Red Team Data"]["Circle"]["Object Center"]["X"],data["Red Team Data"]["Circle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##        redsquare = objpos(data["Red Team Data"]["Square"]["Object Center"]["X"],data["Red Team Data"]["Square"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##        redtriangle = objpos(data["Red Team Data"]["Triangle"]["Object Center"]["X"],data["Red Team Data"]["Triangle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##        
##        bluecircle = objpos(data["Blue Team Data"]["Circle"]["Object Center"]["X"],data["Blue Team Data"]["Circle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##        bluesquare = objpos(data["Blue Team Data"]["Square"]["Object Center"]["X"],data["Blue Team Data"]["Square"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##        bluetriangle = objpos(data["Blue Team Data"]["Triangle"]["Object Center"]["X"],data["Blue Team Data"]["Triangle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##        
##        ball = objpos(data["Ball"]["Object Center"]["X"],data["Ball"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
##        
##        if ((abs(bluecircle.x-redcircle.x))<15 and abs((bluecircle.y-redcircle.y)<15)):
##            sully = 1
##        else:
##            sully = 0
##        pubspeeds("Rover2",0,0,0,sully)
##            #ball.printobj()
##        #redsquare.printobj()
##    else:
##    	print("somthing is Fucked up")
##    
##    return bluesquare



print("Application Starting.....")


##-----------------------------------------------------------

##------------------------------------------------------------

while True:
    
    time.sleep(.555)
##    pubspeeds("Rover2",0,0,0,sully)
    try:
        a = updatejson(ser)
        #time.sleep(2)
        #if ((abs(bluecircle.x-redcircle.x))<15 and abs((bluecircle.y-redcircle.y)<15)):
         #   sully = 1
        #else:
         #   sully = 0
        #print("redsquare")
        # redsquare.printobj()
        #print("redcircle")
        a.printobj()
    
        change = move(a.x,a.y,100,50)
    except:
        print("a")

    magnitude = math.sqrt((change[0]*change[0])+(change[1]*change[1]))
    print(change)

    if(magnitude != 0):
        changeX=(change[0]/magnitude)*300
        changeY=(change[1]/magnitude)*300

        b = vectors(0,changeX,-changeY,0)
        print("motor speeds")
        print(b)
        pubspeeds("Rover1",b[0],b[1],b[2],sully)
        #time.sleep(1)
        pubspeeds("Rover1",0,0,0,sully)
    else:
        pubspeeds("Rover1",0,0,0,sully)

    # ser.close()
    #time.sleep(1)
    # ser = serial.Serial('/dev/serial0',115200) ##declare ser object for serial comms
    #--------------------------------------------------------------------------------------------------------------------------------------
    
