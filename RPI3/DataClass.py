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
class json_data:
    redcircle_x = None
    redcircle_y = None

    redsquare_x = None
    redsquare_y = None

    redtriangle_x = None
    redtriangle_y = None
    
    bluecircle_x = None
    bluecircle_y = None

    bluesquare_x = None
    bluesquare_y = None

    bluetriangle_x = None
    bluetriangle_y = None

    ball_x = None
    ball_y = None
    
    def update(self,data):
        cor_br = corners(data["Corners"][2]["X"],data["Corners"][2]["Y"])
        cor_tr = corners(data["Corners"][3]["X"],data["Corners"][3]["Y"])
        cor_bl = corners(data["Corners"][0]["X"],data["Corners"][0]["Y"])
        cor_tl = corners(data["Corners"][1]["X"],data["Corners"][1]["Y"])
        cval = maxmin_xy(cor_tl.x, cor_tr.x, cor_bl.x, cor_br.x, cor_tl.y, cor_tr.y, cor_bl.y, cor_br.y) #find the max and min values of the corners 
        
        self.redcircle_x = pix2coord_x(data["Red Team Data"]["Circle"]["Object Center"]["X"],cval)
        self.redcircle_y = pix2coord_y(data["Red Team Data"]["Circle"]["Object Center"]["Y"],cval)
        self.redsquare_x = pix2coord_x(data["Red Team Data"]["Square"]["Object Center"]["X"],cval)
        self.redquare_y = pix2coord_y(data["Red Team Data"]["Square"]["Object Center"]["Y"],cval)
        self.redtriangle_x = pix2coord_x(data["Red Team Data"]["Triangle"]["Object Center"]["X"],cval)
        self.redtriangle_y = pix2coord_y(data["Red Team Data"]["Triangle"]["Object Center"]["Y"],cval)
        
        self.bluecircle_x = pix2coord_x(data["Blue Team Data"]["Circle"]["Object Center"]["X"],cval)
        self.bluecircle_y = pix2coord_y(data["Blue Team Data"]["Circle"]["Object Center"]["Y"],cval)
        self.bluesquare_x = pix2coord_x(data["Blue Team Data"]["Square"]["Object Center"]["X"],cval)
        self.bluesquare_y = pix2coord_y(data["Blue Team Data"]["Square"]["Object Center"]["Y"],cval)
        self.bluetriangle_x = pix2coord_x(data["Blue Team Data"]["Triangle"]["Object Center"]["X"],cval)
        self.bluetriangle_y = pix2coord_y(data["Blue Team Data"]["Triangle"]["Object Center"]["Y"],cval)
        
        self.ball_x = pix2coord_x(data["Ball"]["Object Center"]["X"],cval)
        self.ball_y = pix2coord_y(data["Ball"]["Object Center"]["Y"],cval)

        return
    
 
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

def pix2coord_x(pix_x,cval):
##    print(xmin," ",xmax)
##    print(pix_x)
    return ((200.0/(cval.xmax-cval.xmin)*(pix_x-cval.xmin)))

def pix2coord_y(pix_y,cval):
##    print(ymin," ",ymax)
##    print(pix_y)
    return (100.0/(cval.ymax-cval.ymin)*(pix_y-cval.ymin))
while True:
    loc_data = json_data()
    print("this was ran")


    
    

