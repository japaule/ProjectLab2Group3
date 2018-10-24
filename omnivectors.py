import math

theta = 0
fx = 1
fy = 1
x = 0

def vectors( theta, fx, fy, x):
    faTop = (-fx*math.sin(math.radians(theta+180))+fx*math.sin(math.radians(theta+60))+fy*math.cos(math.radians(theta+180))-fy*math.cos(math.radians(theta+60))-x*math.cos(math.radians(theta+180))*math.sin(math.radians(theta+60))+x*math.cos(math.radians(theta+60))*math.sin(math.radians(theta+180)))
    fbTop = (fx*math.sin(math.radians(theta+300))-fx*math.sin(math.radians(theta+60))-fy*math.cos(math.radians(theta+300))+fy*math.cos(math.radians(theta+60))+x*math.cos(math.radians(theta+300))*math.sin(math.radians(theta+60))-x*math.cos(math.radians(theta+60))*math.sin(math.radians(theta+300)))
    fcTop = (fx*math.sin(math.radians(theta+180))-fx*math.sin(math.radians(theta+300))-fy*math.cos(math.radians(theta+180))+fy*math.cos(math.radians(theta+60))+x*math.cos(math.radians(theta+180))*math.sin(math.radians(theta+300))-x*math.cos(math.radians(theta+300))*math.sin(math.radians(theta+180)))
    bot = (math.cos(math.radians(theta+180))*math.sin(math.radians(theta+300))-math.cos(math.radians(theta+180))*math.sin(math.radians(theta+60))-math.cos(math.radians(theta+300))*math.sin(math.radians(theta+180))+math.cos(math.radians(theta+300))*math.sin(math.radians(theta+60))+math.cos(math.radians(theta+60))*math.sin(math.radians(theta+180))-math.cos(math.radians(theta+60))*math.sin(math.radians(theta+300)))


    fa = faTop/bot
    fb = fbTop/bot
    fc = fcTop/bot

    return [fa,fb,fc]

def orentation(theta, x, y):
    x=50-x

    nTheta = math.degrees(math.atan(x/y))
    nTheta = nTheta - theta
    return nTheta

def move(cx, cy, nx, ny):
        changeX = nx - cx
        changeY = ny - cy

        if(changeX < 5)
            changeX = 0

        if(changeY < 5)
            changeY = 0

        return [changeX, changeY]


change = move(100,50,50,75)

magnitude = math.sqrt((change[0]*change[0])+(change[1]*change[1]))

changeX=(change[0]/magnitude)*300
changeY=(change[1]/magnitude)*300

print(changeX)
print(changeY)
print(vectors(theta,changeX,changeY,x))



    
