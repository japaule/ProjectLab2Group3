## Main file.....
## Project Lab II
## Group Members:
## James Paule
## Jacob Saldua
## Cole Lewis
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

##    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##    data = r.json()
##    ldata.update(data)
##    if ((abs(ldata.bluecircle_x-ldata.redcircle_x))<15 and abs((ldata.bluecircle_y-ldata.redcircle_y)<15)):
##        sully = 1
##    else:
##        sully = 0
    #print(data["Blue Team Data"]["Square"]["Object Center"]["X"])
    #print(ldata.bluecircle_x," ", ldata.bluecircle_y)
    #print(ldata.redcircle_x," ", ldata.redcircle_y)
    #print(ldata.ball_x," ", ldata.ball_y)



    #Rover 2 go to ball (BlueCircle)
    #---------------------------------------------------------------------------------------------------------
##    startx = ldata.redsquare_x
##    starty = ldata.redsquare_y
##    print("to ball")
##    cordX = ldata.ball_x+10
##    cordY = ldata.ball_y
##    last = moverover("r","square",cordX,cordY, "Rover2", -1, -1)
##    print("touch ball")
##    cordX = ldata.ball_x
##    cordY = ldata.ball_y
##    last = moverover("r","square",cordX,cordY, "Rover2", last[0], last[1])
##    print("backup")
##    cordX = cordX+15
##    cordY = cordY
##    last = moverover("r","square",cordX,cordY, "Rover2", last[0], last[1] )
##    print("to start")
##    cordX = startx
##    cordY = starty
##    last = moverover("r","square",cordX,cordY, "Rover2", last[0], last[1])
    print("to ball")
    cordX = ldata.ball_x+7
    cordY = ldata.ball_y
    last = moverover("r","circle",cordX,cordY, "Rover1", -1, -1)
##    print("touch ball")
##    cordX = ldata.ball_x-10
##    cordY = ldata.ball_y
##    last = moverover("r","circle",cordX,cordY, "Rover1", last[0], last[1])
    print("to goal")
    cordX = 1
    cordY = 50
    last = moverover("r","circle",cordX,cordY, "Rover1", last[0], last[1])
##    ldatax = ldata.bluecircle_x
##    ldatay = ldata.bluecircle_y
##    while magnitude:
##        print(cordX,cordY)
##        r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##        data = r.json()
##        ldata.update(data)
##        datax=ldata.bluecircle_x
##        datay=ldata.bluecircle_y
##        print(datax," ", datay)
##        if(not(abs(ldatax-ldata.bluecircle_x) < 30 and abs(ldatay-ldata.bluecircle_y) < 20)):
##            if(not(change(ldatax,ldatay,ldata.bluesquare_x,ldata.bluesquare_y))):
##                datax = ldata.bluesquare_x
##                datay = ldata.bluesquare_y
##                magnitude = move("Rover1", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover1", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("square")
##            if(not(change(ldatax,ldatay,ldata.bluetriangle_x,ldata.bluetriangle_y))):
##                datax = ldata.bluetriangle_x
##                datay = ldata.bluetriangle_y
##                magnitude = move("Rover1", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover1", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("triangle")
##            
##        else:
##            magnitude = move("Rover1", datax,0,cordX,0)
##            time.sleep(.5)
##            magnitude = magnitude + move("Rover1", 0,datay,0,cordY)
##            ldatax = datax
##            ldatay = datay
##        time.sleep(.5)
##    magnitude = 1;



    #Rover 2 Move out of the way (BlueCircle)
    #-------------------------------------------------------------------------------------------------------------
    cordX = 150
    cordY = 25
##    ldatax = ldata.bluecircle_x
##    ldatay = ldata.bluecircle_y
##    while magnitude:
##        r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##        data = r.json()
##        ldata.update(data)
##        datax=ldata.bluecircle_x
##        datay=ldata.bluecircle_y
##        print(datax," ", datay)
##        if(not(abs(ldatax-ldata.bluecircle_x) <20 and abs(ldatay-ldata.bluecircle_y) <10)):
##            if(not(change(ldatax,ldatay,ldata.bluesquare_x,ldata.bluesquare_y))):
##                datax = ldata.bluesquare_x
##                datay = ldata.bluesquare_y
##                magnitude = move("Rover2", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover2", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("square")
##            if(not(change(ldatax,ldatay,ldata.bluetriangle_x,ldata.bluetriangle_y))):
##                datax = ldata.bluetriangle_x
##                datay = ldata.bluetriangle_y
##                magnitude = move("Rover2", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover2", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("triangle")
##            magnitude = move("Rover2", datax,0,cordX,0)
##        else:
##            magnitude = move("Rover2", datax,0,cordX,0)
##            time.sleep(.5)
##            magnitude = magnitude + move("Rover2", 0,datay,0,cordY)
##            ldatax = datax
##            ldatay = datay
##        time.sleep(.5)
##        print(datax," ", datay)



    #Rover 1 go to ball (BlueSquare)
    #--------------------------------------------------------------------------------------------------------
    cordX = ldata.ball_x+10
    cordY = ldata.ball_y
##    ldatax = ldata.bluesquare_x
##    ldatay = ldata.bluesquare_y
##    while magnitude:
##        print(cordX,cordY)
##        r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##        data = r.json()
##        ldata.update(data)
##        datax=ldata.bluesquare_x
##        datay=ldata.bluesquare_y
##        print(datax," ", datay)
##        if(not(abs(ldatax-ldata.bluesquare_x) < 30 and abs(ldatay-ldata.bluesquare_y) < 20)):
##            if(not(change(ldatax,ldatay,ldata.bluecircle_x,ldata.bluecircle_y))):
##                datax = ldata.bluecircle_x
##                datay = ldata.bluecircle_y
##                magnitude = move("Rover1", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover1", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("circle")
##            if(not(change(ldatax,ldatay,ldata.bluetriangle_x,ldata.bluetriangle_y))):
##                datax = ldata.bluetriangle_x
##                datay = ldata.bluetriangle_y
##                magnitude = move("Rover1", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover1", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("triangle")
##            
##        else:
##            magnitude = move("Rover1", datax,0,cordX,0)
##            time.sleep(.5)
##            magnitude = magnitude + move("Rover1", 0,datay,0,cordY)
##            ldatax = datax
##            ldatay = datay
##        time.sleep(.5)
##    magnitude = 1;



#Rover 1 go to goal
#------------------------------------------------------------------------------------------------------
    cordX = 3
    cordY = 50
##    ldatax = ldata.bluesquare_x
##    ldatay = ldata.bluesquare_y
##    while magnitude:
##        r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
##        data = r.json()
##        ldata.update(data)
##        datax=ldata.bluesquare_x
##        datay=ldata.bluesquare_y
##        print(datax," ", datay)
##        if(not(abs(ldatax-ldata.bluesquare_x) <20 and abs(ldatay-ldata.bluesquare_y) <10)):
##            if(not(change(ldatax,ldatay,ldata.bluecircle_x,ldata.bluecircle_y))):
##                datax = ldata.bluecircle_x
##                datay = ldata.bluecircle_y
##                magnitude = move("Rover1", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover1", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("circle")
##            if(not(change(ldatax,ldatay,ldata.bluetriangle_x,ldata.bluetriangle_y))):
##                datax = ldata.bluetriangle_x
##                datay = ldata.bluetriangle_y
##                magnitude = move("Rover1", datax,0,cordX,0)
##                time.sleep(.5)
##                magnitude = move("Rover1", 0,datay,0,cordY)
##                ldatax = datax
##                ldatay = datay
##                print("triangle")
##            magnitude = move("Rover1", datax,0,cordX,0)
##        else:
##            magnitude = move("Rover1", datax,0,cordX,0)
##            time.sleep(.5)
##            magnitude = magnitude + move("Rover1", 0,datay,0,cordY)
##            ldatax = datax
##            ldatay = datay
##        time.sleep(.5)
##        print(datax," ", datay)
##    magnitude = 1;

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

