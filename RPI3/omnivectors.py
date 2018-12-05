import math

from Mqtt import *
import time
import json
from DataClass import *
import time
import requests

theta = 0
fx = 1
fy = 1
x = 0

def vectors( theta, fx, fy, x):
    
    temp = fx%2
    if (temp<1):
        fx = fx - temp
    else:
        fx = fx +(2-temp)
        
    temp = fy%2
    if (temp<1):
        fy = fy - temp
    else:
        fy = fy +(2-temp)
    
    faTop = (-fx*math.sin(math.radians(theta+180))+fx*math.sin(math.radians(theta+60))+fy*math.cos(math.radians(theta+180))-fy*math.cos(math.radians(theta+60))-x*math.cos(math.radians(theta+180))*math.sin(math.radians(theta+60))+x*math.cos(math.radians(theta+60))*math.sin(math.radians(theta+180)))
    fbTop = (fx*math.sin(math.radians(theta+300))-fx*math.sin(math.radians(theta+60))-fy*math.cos(math.radians(theta+300))+fy*math.cos(math.radians(theta+60))+x*math.cos(math.radians(theta+300))*math.sin(math.radians(theta+60))-x*math.cos(math.radians(theta+60))*math.sin(math.radians(theta+300)))
    fcTop = (fx*math.sin(math.radians(theta+180))-fx*math.sin(math.radians(theta+300))-fy*math.cos(math.radians(theta+180))+fy*math.cos(math.radians(theta+60))+x*math.cos(math.radians(theta+180))*math.sin(math.radians(theta+300))-x*math.cos(math.radians(theta+300))*math.sin(math.radians(theta+180)))
    bot = (math.cos(math.radians(theta+180))*math.sin(math.radians(theta+300))-math.cos(math.radians(theta+180))*math.sin(math.radians(theta+60))-math.cos(math.radians(theta+300))*math.sin(math.radians(theta+180))+math.cos(math.radians(theta+300))*math.sin(math.radians(theta+60))+math.cos(math.radians(theta+60))*math.sin(math.radians(theta+180))-math.cos(math.radians(theta+60))*math.sin(math.radians(theta+300)))


    fa = faTop/bot
    fb = fbTop/bot
    fc = fcTop/bot
##    ma = max(fa,fb,fc)
##    mi = min(fa,fb,fc)
##    if (fa == ma):
##        fa = fa*.93
##    elif (fb == ma):
##        fb = fb*.93
##    elif (fc == ma):
##        fc = fc*.93
##    if (fa == mi):
##        fa = fa*1.05
##    elif (fb == mi):
##        fb = fb*1.05
##    elif (fc == mi):
##        fc = fc*1.05
    
    

    return [linear(int(fa)),linear(int(fb)),linear(int(fc))]

def orentation(theta, x, y):
    y=50-y

    nTheta = math.degrees(math.atan(y/x))
    nTheta = nTheta - theta
    temp = nTheta%25
    if (temp<12):
        nTheta = nTheta - temp
    else:
        nTheta = nTheta +(25-temp)
    return int(nTheta)

def move(rover, cx, cy, nx, ny):
    changeX = nx - cx
    changeY = ny - cy

    if(abs(changeX) < 4):
        changeX = 0
    if(abs(changeY) < 1):
        changeY = 0
        
    magnitude = math.sqrt((changeX*changeX)+(changeY*changeY))
    
    if(magnitude != 0):
        changeX=(changeX/magnitude)*300
        changeY=(changeY/magnitude)*300
        
        if(changeX < 0 ):
            pubspeeds(rover,-500,500,0,0)
            print("-X")
        elif(changeX > 0):
            pubspeeds(rover,500,-500,0,0)
            print("+X")
        elif(changeY < 0):
            pubspeeds(rover,-100,-100,217,0)
            print("-Y")
        elif(changeY > 0):
            pubspeeds(rover,100,100,-215,0)
            print("+Y")
            
            

        #b = vectors(theta,changeX,-changeY,0)
##        print("motor speeds")
##        print(b)
##        pubspeeds(rover,int(b[0]),int(b[1]),int(b[2]),0)
        t=(magnitude/223) * 2
        #if (t < .15):
            #t = .15
        time.sleep(t)
        #pubspeeds(rover,0,0,0,0)
    else:
        pubspeeds(rover,0,0,0,0)

    return magnitude
    
def turn(theta):
    t = theta/360
    t = t * 5
    return t

def change( cx, cy, nx, ny):
    changeX = nx - cx
    changeY = ny - cy

    if(abs(changeX) < 1):
        changeX = 0

    if(abs(changeY) < 1):
        changeY = 0
        
    magnitude = math.sqrt((changeX*changeX)+(changeY*changeY))
    
    return magnitude

def linear(a):
    return a
    if(a>=5 and a<15):
        return 50
    elif(a>=15 and a<30):
        return 50
    elif(a>=30 and a<50):
        return 70
    elif(a>=50 and a<75):
        return 105
    elif(a>=75 and a<100):
        return 125
    elif(a>=100 and a<115):
        return 135
    elif(a>=0):
        return a 
    a = abs(a)
    if(a>=5 and a<15):
        return -50
    elif(a>=15 and a<30):
        return -50
    elif(a>=30 and a<50):
        return -70
    elif(a>=50 and a<75):
        return -105
    elif(a>=75 and a<100):
        return -125
    elif(a>=100 and a<115):
        return -135
    elif(a>0):
        return -a
    
    
def moverover(color, shape, cordX, cordY, rover, lastx, lasty):
    
    magnitude = 1
    ldata = json_data()
    r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
    data = r.json()
    ldata.update(data)
    if(lastx == -1 or lasty == -1):
        if(color == "b"):
            if(shape == "triangle"):
                ldatax=ldata.bluetriangle_x
                ldatay=ldata.bluetriangle_y
            
            if(shape == "circle"):
                ldatax=ldata.bluecircle_x
                ldatay=ldata.bluecircle_y
            
            if(shape == "square"):
                ldatax=ldata.bluesquare_x
                ldatay=ldata.bluesquare_y
        
        if(color == "r"):
            if(shape == "triangle"):
                ldatax=ldata.redtriangle_x
                ldatay=ldata.bluetriangle_y
            
            if(shape == "circle"):
                ldatax=ldata.redcircle_x
                ldatay=ldata.redcircle_y
            
            if(shape == "square"):
                ldatax=ldata.redsquare_x
                ldatay=ldata.redsquare_y
    else:
        ldatax = lastx
        ldatay = lasty
    print(ldatax, " ", ldatay)
    print(" ")
    
    while magnitude:
        r = requests.get("http://192.168.137.1:8001/FieldData/GetData")
        data = r.json()
        ldata.update(data)
        
        if(color == "b"):
            if(shape == "triangle"):
                datax=ldata.bluetriangle_x
                datay=ldata.bluetriangle_y
                alt1x=ldata.bluecircle_x
                alt1y=ldata.bluecircle_y
                alt2x=ldata.bluesquare_x
                alt2y=ldata.bluesquare_y
            
            elif(shape == "circle"):
                datax=ldata.bluecircle_x
                datay=ldata.bluecircle_y
                alt1x=ldata.bluetriangle_x
                alt1y=ldata.bluetriangle_y
                alt2x=ldata.bluesquare_x
                alt2y=ldata.bluesquare_y
            
            elif(shape == "square"):
                datax=ldata.bluesquare_x
                datay=ldata.bluesquare_y
                alt1x=ldata.bluecircle_x
                alt1y=ldata.bluecircle_y
                alt2x=ldata.bluetriangle_x
                alt2y=ldata.bluetriangle_y
            else:
                return "shape error"
        
        elif(color == "r"):
            if(shape == "triangle"):
                datax=ldata.redtriangle_x
                datay=ldata.redtriangle_y
                alt1x=ldata.redcircle_x
                alt1y=ldata.redcircle_y
                alt2x=ldata.redsquare_x
                alt2y=ldata.redsquare_y
            
            elif(shape == "circle"):
                datax=ldata.redcircle_x
                datay=ldata.redcircle_y
                alt1x=ldata.redtriangle_x
                alt1y=ldata.redtriangle_y
                alt2x=ldata.redsquare_x
                alt2y=ldata.redsquare_y
            
            elif(shape == "square"):
                datax=ldata.redsquare_x
                datay=ldata.redsquare_y
                alt1x=ldata.redcircle_x
                alt1y=ldata.redcircle_y
                alt2x=ldata.redtriangle_x
                alt2y=ldata.redtriangle_y
            else:
                return "shape error"
        else:
            return "color error"

        print(datax," ", datay)
        if(not(abs(ldatax-datax) < 35 and abs(ldatay-datay) < 20)):
            if((abs(ldatax-alt1x) < 12 and abs(ldatay-alt1y) < 8)):
                datax = alt1x
                datay = alt1y
                magnitude = move(rover, datax,0,cordX,0)
                #time.sleep(.5)
                magnitude = magnitude + move(rover, 0,datay,0,cordY)
                print(ldatax," ", ldatay)
                ldatax = datax
                ldatay = datay
                print("alt1")
                print(datax," ", datay)
            elif((abs(ldatax-alt2x) < 12 and abs(ldatay-alt2y) < 8)):
                datax = alt2x
                datay = alt2y
                magnitude = move(rover, datax,0,cordX,0)
                #time.sleep(.5)
                magnitude = magnitude +  move(rover, 0,datay,0,cordY)
                print(ldatax," ", ldatay)
                ldatax = datax
                ldatay = datay
                print("alt2")
                print(datax," ", datay)
            else:
                time.sleep(2)
                mag1 = change(ldatax,ldatay,alt1x,alt1y)
                mag2 = change(ldatax,ldatay,alt2x,alt2y)
                mag3 = change(ldatax,ldatay,datax,datay)
                if(mag1<mag2 and mag1<mag3):
                    print("Error alt1")
                    datax = alt1x
                    datay = alt1y
                    magnitude = move(rover, datax,0,cordX,0)
                    #time.sleep(.5)
                    magnitude = magnitude + move(rover, 0,datay,0,cordY)
                    print(ldatax," ", ldatay)
                    ldatax = datax
                    ldatay = datay
                    print("alt1")
                    print(datax," ", datay)
                if(mag2<mag1 and mag2<mag3):
                    print("Error alt2")
                    datax = alt2x
                    datay = alt2y
                    magnitude = move(rover, datax,0,cordX,0)
                    #time.sleep(.5)
                    magnitude = magnitude +  move(rover, 0,datay,0,cordY)
                    print(ldatax," ", ldatay)
                    ldatax = datax
                    ldatay = datay
                    print("alt2")
                    print(datax," ", datay)
                if(mag3<mag1 and mag3<mag2):
                    print("Error normal")
                    magnitude = move(rover, datax,0,cordX,0)
                    #time.sleep(.5)
                    magnitude = magnitude + move(rover, 0,datay,0,cordY)
                    ldatax = datax
                    ldatay = datay
                
            
        else:
            magnitude = move(rover, datax,0,cordX,0)
            #time.sleep(.5)
            magnitude = magnitude + move(rover, 0,datay,0,cordY)
            ldatax = datax
            ldatay = datay
        #time.sleep(.5)
        print("------------------------------------------------------------")
    return [ldatax,ldatay]
    
    

    
