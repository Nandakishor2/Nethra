import cv2
import facemodule as fm
import math
import numpy as np

class distancefinder():
    def __init__(self):
        
        self.x=[300,245,200,170,145,130,112,103,93,87,80,75,70,67,62,59,57]
        self.y=[20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
        self.coff = np.polyfit(self.x,self.y,2)
    def finddistance(self,lmlist):
        x1,y1= lmlist[336][1],lmlist[336][2]
        x2,y2 =lmlist[107][1],lmlist[107][2]
        distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        a,b,c = self.coff
        distancecm = a*distance**2 + b*distance+c
        return distancecm

