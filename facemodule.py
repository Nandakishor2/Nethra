from concurrent.futures import process
from unittest import result
from cv2 import FONT_HERSHEY_COMPLEX
import mediapipe as mp

import cv2
import math
import csv

class facedetection():
    
    def __init__(self,mode=False,maxface = 1,refinelm = False,detectioncon = 0.5,trackingcon = 0.5):
        self.mode = mode
        self.maxface = maxface
        self.refinelm = refinelm
        self.detectioncon = detectioncon
        self.trackingcon = trackingcon
        self.mpdraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.facemesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)
        self.drawSpec = self.mpdraw.DrawingSpec(thickness=1, circle_radius=2)
    
    def findfaces(self,img,draw = True):
        imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.facemesh.process(imgrgb)
        if self.results.multi_face_landmarks:
            for facelms in self.results.multi_face_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, facelms, self.mpFaceMesh.FACEMESH_CONTOURS,self.drawSpec,self.drawSpec)       
        return img
    def findfacelm(self,img,draw = False):
        lmlist = []
        if self.results.multi_face_landmarks:
            for self.facelms in self.results.multi_face_landmarks:
                for id,lm in  enumerate(self.facelms.landmark):
                    h,w,c = img.shape
                    x,y = int(lm.x*w),int(lm.y*h)
                    lmlist.append([id,x,y])
                    if draw:
                        cv2.putText(img,str(id),(x,y),FONT_HERSHEY_COMPLEX,0.4,(0,255,255),1)   
        return lmlist
