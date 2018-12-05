## this file contains functions and classes that rpiserialcomm uses to parse and translate to xy coordinates

class objpos:
    def __init__(self,x,y,xmin,xmax,ymin,ymax):
        self.x = pix2coord_x(x,xmax,xmin)
        self.y = pix2coord_y(y,ymax,ymin)
    def update(self,x,y):
        self.x = x
        self.y = y
    def printobj(self):
        print(self.x," ",self.y)
    
 
class corners:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def printobj(self):
        print(self.x," ",self.y)
    
class maxmin_xy:
    def __init__(self,x1,x2,x3,x4,y1,y2,y3,y4):
        self.xmax = max(x1,x2,x3,x4)
        self.ymax = max(y1,y2,y3,y4)
        self.xmin = min(x1,x2,x3,x4)
        self.ymin = min(y1,y2,y3,y4)

def pix2coord_x(pix_x,xmax,xmin):
##    print(xmin," ",xmax)
##    print(pix_x)
    return ((200.0/(xmax-xmin)*(pix_x-xmin)))

def pix2coord_y(pix_y,ymax,ymin):
##    print(ymin," ",ymax)
##    print(pix_y)
    return (100.0/(ymax-ymin)*(pix_y-ymin))


    
    

