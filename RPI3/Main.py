## This application is designed to ping and parse data from TTUSwarmField in json format.
## Additonally, it converts the pixel data to coordinates
## Project Lab II
## Group Members:
## James Paule
## Jacob Saldua
## Cole Lewis

from pix2coord import *
from Mqtt import *

sully = 0

print("Application Starting.....")

##Serial Comm Setup
print("Serial Comm setup...")
ser = serial.Serial('/dev/serial0',115200) ##declare ser object for serial comms
time.sleep(1)
mqtt_setup() 							##Set up for mqtt 
time.sleep(1)
##-----------------------------------------------------------
## declare objects 
cor_br = corners(0,0)
cor_tr = corners(0,0)
cor_bl = corners(0,0)
cor_tl = corners(0,0)

redcircle = objpos(0,0,0,0,0,0)
redsquare = objpos(0,0,0,0,0,0)
redtriangle = objpos(0,0,0,0,0,0)

bluecircle = objpos(0,0,0,0,0,0)
bluesquare = objpos(0,0,0,0,0,0)
bluetriangle = objpos(0,0,0,0,0,0)

ball = objpos(0,0,0,0,0,0)
##------------------------------------------------------------

while True:
    updatejson(ser)
    time.sleep(.25)
    pubspeeds("Rover1",100,-200,100,sully)
    if ((abs(ball.x-redcircle.x))<5 && abs((ball.y-redcircle.y)<5)):
            sully = 1
    else:
            sully = 0


    #ser.close()
        
def updatejson(ser):	## used to fetch json data, parse and translate into x,y coordinates
    # Serial begin with esp8266--------------------------------------------------
    if ser.inWaiting() > 0:
        rawdata = ser.readline()
        rawdata = rawdata.decode('ASCII')
        data = json.loads(rawdata)
		##parse data and save into objects
        # ------------------------------------------------------------
        cor_br = corners(data["Corners"][2]["X"],data["Corners"][2]["Y"])
        cor_tr = corners(data["Corners"][3]["X"],data["Corners"][3]["Y"])
        cor_bl = corners(data["Corners"][0]["X"],data["Corners"][0]["Y"])
        cor_tl = corners(data["Corners"][1]["X"],data["Corners"][1]["Y"])
        cval = maxmin_xy(cor_tl.x, cor_tr.x, cor_bl.x, cor_br.x, cor_tl.y, cor_tr.y, cor_bl.y, cor_br.y) #find the max and min values of the corners 
        
        redcircle = objpos(data["Red Team Data"]["Circle"]["Object Center"]["X"],data["Red Team Data"]["Circle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
        redsquare = objpos(data["Red Team Data"]["Square"]["Object Center"]["X"],data["Red Team Data"]["Square"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
        redtriangle = objpos(data["Red Team Data"]["Triangle"]["Object Center"]["X"],data["Red Team Data"]["Triangle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
        
        bluecircle = objpos(data["Blue Team Data"]["Circle"]["Object Center"]["X"],data["Blue Team Data"]["Circle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
        bluesquare = objpos(data["Blue Team Data"]["Square"]["Object Center"]["X"],data["Blue Team Data"]["Square"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
        bluetriangle = objpos(data["Blue Team Data"]["Triangle"]["Object Center"]["X"],data["Blue Team Data"]["Triangle"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
        
        ball = objpos(data["Ball"]["Object Center"]["X"],data["Ball"]["Object Center"]["Y"],cval.xmin,cval.xmax,cval.ymin,cval.ymax)
        
        ball.printobj()
        return        
##--------------------------------------------------------------------------------------------------------------------------------------------------------
    
