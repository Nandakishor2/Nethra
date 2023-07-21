import cv2
import facemodule as fm
import math
import numpy as np
cap = cv2.VideoCapture(1)

detector = fm.facedetection()
x=[300,245,200,170,145,130,112,103,93,87,80,75,70,67,62,59,57]
y=[20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
coff = np.polyfit(x,y,2)
while True:
    lmlist = []
    success,img = cap.read()
    img = detector.findfaces(img,draw=False)
    lmlist = detector.findfacelm(img,draw=False)
    x1,y1= lmlist[336][1],lmlist[336][2]
    x2,y2 =lmlist[107][1],lmlist[107][2]
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    a,b,c = coff
    distancecm = a*distance**2 + b*distance+c
    print(distance,int(distancecm))
    
    cv2.imshow("Success",img)
    
    cv2.waitKey(10)