import cv2
import mediapipe as mp

class posedetector():
      
      def __init__(self,mode=False,modcomplex = 1,smlm = True,enableseg = True,smoothseg = True,detectioncon = 0.5,trackingcon = 0.5) :
            
            
            self.mode = mode
            self.modcomplex = modcomplex
            self.smlm  =  smlm
            self.enableseg = enableseg
            self.smoothseg = smoothseg
            self.detectioncon = detectioncon
            self.trackingcon = trackingcon
            self.mpdraw = mp.solutions.drawing_utils
            self.mppose = mp.solutions.pose
            self.pose = self.mppose.Pose(self.mode,self.modcomplex,self.smlm,self.enableseg ,self.smoothseg,self.detectioncon,self.trackingcon)

      def findpose(self,img,draw = True):
            imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            self.results = self.pose.process(imgrgb)
            if self.results.pose_landmarks:
                  if draw:
                        self.mpdraw.draw_landmarks(img,self.results.pose_landmarks,self.mppose.POSE_CONNECTIONS)
            
            return img
      def findpositions(self,img,draw=True):
            lmlist = []
            if self.results.pose_landmarks:
                  for id,ln in enumerate(self.results.pose_landmarks.landmark):
                        h,w,c = img.shape
                        
                        cx,cy = int(ln.x*w),int(ln.y*h)
                        lmlist.append([id,cx,cy])
                        if draw:
                              cv2.circle(img,(lmlist[0][1],lmlist[0][2]),5,(255,0,0),cv2.FILLED)

            return lmlist
            
      


