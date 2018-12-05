## Main file.....
## Project Lab II
## Group Members:
## James Paule
## Jacob Saldua
## Cole Lewis
<<<<<<< HEAD
try:
    #from pix2coord import *
    from Mqtt import *
    from omnivectors import *
    #from rpiserialcomm import *
    #import serial
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

    print("Mqtt setup successful....")


    ##-----------------------------------------------------------

    ##------------------------------------------------------------

    #while True:
        
    time.sleep(.25)
    ##    pubspeeds("Rover2",0,0,0,sully)

    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
    data = r.json()
    ldata.update(data)
    if ((abs(ldata.bluecircle_x-ldata.redcircle_x))<15 and abs((ldata.bluecircle_y-ldata.redcircle_y)<15)):
        sully = 1
    else:
        sully = 0
    #print(data["Blue Team Data"]["Square"]["Object Center"]["X"])
    #print(ldata.bluecircle_x," ", ldata.bluecircle_y)
    #print(ldata.redcircle_x," ", ldata.redcircle_y)
    #print(ldata.ball_x," ", ldata.ball_y)
    cordX = ldata.ball_x+10
    cordY = ldata.ball_y
    ldatax = ldata.bluesquare_x
    ldatay = ldata.bluesquare_y
    while magnitude:
        print(cordX,cordY)
        r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
        data = r.json()
        ldata.update(data)
        datax=ldata.bluesquare_x
        datay=ldata.bluesquare_y
        print(datax," ", datay)
        if(not(abs(ldatax-ldata.bluesquare_x) < 30 and abs(ldatay-ldata.bluesquare_y) < 20)):
            if(not(change(ldatax,ldatay,ldata.bluecircle_x,ldata.bluecircle_y))):
                datax = ldata.bluecircle_x
                datay = ldata.bluecircle_y
                magnitude = move("Rover1", datax,0,cordX,0)
                time.sleep(.5)
                magnitude = move("Rover1", 0,datay,0,cordY)
                ldatax = datax
                ldatay = datay
                print("circle")
            if(not(change(ldatax,ldatay,ldata.bluetriangle_x,ldata.bluetriangle_y))):
                datax = ldata.bluetriangle_x
                datay = ldata.bluetriangle_y
                magnitude = move("Rover1", datax,0,cordX,0)
                time.sleep(.5)
                magnitude = move("Rover1", 0,datay,0,cordY)
                ldatax = datax
                ldatay = datay
                print("triangle")
            
        else:
            magnitude = move("Rover1", datax,0,cordX,0)
            time.sleep(.5)
            magnitude = magnitude + move("Rover1", 0,datay,0,cordY)
            ldatax = datax
            ldatay = datay
        time.sleep(.5)
    magnitude = 1;

    cordX = 3
    cordY = 50
    ldatax = ldata.bluesquare_x
    ldatay = ldata.bluesquare_y
    while magnitude:
        r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
        data = r.json()
        ldata.update(data)
        datax=ldata.bluesquare_x
        datay=ldata.bluesquare_y
        print(datax," ", datay)
        if(not(abs(ldatax-ldata.bluesquare_x) <20 and abs(ldatay-ldata.bluesquare_y) <10)):
            if(not(change(ldatax,ldatay,ldata.bluecircle_x,ldata.bluecircle_y))):
                datax = ldata.bluecircle_x
                datay = ldata.bluecircle_y
                magnitude = move("Rover1", datax,0,cordX,0)
                time.sleep(.5)
                magnitude = move("Rover1", 0,datay,0,cordY)
                ldatax = datax
                ldatay = datay
                print("circle")
            if(not(change(ldatax,ldatay,ldata.bluetriangle_x,ldata.bluetriangle_y))):
                datax = ldata.bluetriangle_x
                datay = ldata.bluetriangle_y
                magnitude = move("Rover1", datax,0,cordX,0)
                time.sleep(.5)
                magnitude = move("Rover1", 0,datay,0,cordY)
                ldatax = datax
                ldatay = datay
                print("triangle")
            magnitude = move("Rover1", datax,0,cordX,0)
        else:
            magnitude = move("Rover1", datax,0,cordX,0)
            time.sleep(.5)
            magnitude = magnitude + move("Rover1", 0,datay,0,cordY)
            ldatax = datax
            ldatay = datay
        time.sleep(.5)
        print(datax," ", datay)
    magnitude = 1;

    ##cordX = 100
    ##cordY = 85
    ##while magnitude:
    ##    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
    ##    data = r.json()
    ##    ldata.update(data)
    ##    print(ldata.bluesquare_x," ", ldata.bluesquare_y)
    ##    magnitude = move("Rover1", ldata.bluesquare_x,0,cordX,0)
    ##    time.sleep(.25)
    ##    magnitude = move("Rover1", 0,ldata.bluesquare_y,0,cordY)
    ##    time.sleep(.25)
    ##magnitude = 1;
    ##while magnitude:
    ##    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
    ##    data = r.json()
    ##    ldata.update(data)
    ##    print(ldata.bluesquare_x," ", ldata.bluesquare_y)
    ##    magnitude = move("Rover1", 0,ldata.bluesquare_y,0,cordY)
    ##    time.sleep(.25)
    ##magnitude = 1;


        
            
    ##    cordX = 100
    ##    cordY = 80
    ##    while magnitude:
    ##        print(ldata.bluesquare_x," ", ldata.bluesquare_y)
    ##        magnitude = move("Rover1", ldata.bluesquare_x,ldata.bluesquare_y,cordX,cordY)
    ##    magnitude = 1;
    ##        
    ##    cordX = ldata.ball_x
    ##    cordY = ldata.ball_y
    ##    while magnitude:
    ##        print(ldata.bluesquare_x," ", ldata.bluesquare_y)
    ##        magnitude = move("Rover2", ldata.bluecircle_x,ldata.bluescircle_y,cordX,cordY)
    ##    magnitude = 1;
    ##        
    ##    cordX = 15
    ##    cordY = 50
    ##    while magnitude:
    ##        print(ldata.bluesquare_x," ", ldata.bluesquare_y)
    ##        magnitude = move("Rover2", ldata.bluecircle_x,ldata.bluescircle_y,cordX,cordY)
    ##    magnitude = 1;

        
    ##    ntheta = orentation(theta, ldata.bluesquare_x, ldata.bluesquare_y)
    ##    theta = theta + ntheta
    ##    print(theta)
    ##    t = turn(ntheta)
    ##    if t > .1:
    ##        pubspeeds("Rover1",200,200,200,sully)
    ##        time.sleep(t)
    ##    elif t < -.1:
    ##        pubspeeds("Rover1",-200,-200,-200,sully)
    ##        time.sleep(abs(t))
    ##    pubspeeds("Rover1",0,0,0,sully)


    ##    except:
    ##        	print("Houston We Have A Problem")

           
        #--------------------------------------------------------------------------------------------------------------------------------------

finally:
    pubspeeds("Rover1",0,0,0,0)
    pubspeeds("Rover2",0,0,0,0)
    pubspeeds("Rover3",0,0,0,0)
=======

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
    
>>>>>>> 5e87f194f2bbe21edf1961c00226e3fc689fb17d
