#File used to communicate with esp8266 to gather json location data
# REV 1.1

import time
import serial
import json
import os
from pix2coord import *
ser=None

##class definition of objects on field
##------------------------------------
def updatejson(ser):
            # Serial begin with esp8266--------------------------------------------------
            if ser.inWaiting() > 0:
                rawdata = ser.readline()
                rawdata = rawdata.decode('ASCII')
                data = json.loads(rawdata)
                
##                parse data and save into objects
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
        
##        except KeyboardInterrupt: 
##            print ("Exiting Program")
##        ##except:
##        ##    print ("Error Occurs, Exiting Program")
##
##        finally:
##            ser.close()
##            pass

