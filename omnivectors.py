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

    return [changeX, changeY]

    
