import cv2
import facemodule
import distancemodule
import humandetectionmodule
import talk
import time

def main():
    cap = cv2.VideoCapture(1)
    face = facemodule.facedetection()
    dis = distancemodule.distancefinder()
    human = humandetectionmodule.posedetector()
    text = talk.speaker()
    text.speak("Initializing Nethra")
    time.sleep(1)
    text.speak("Almost ready getting some dependencies")
    time.sleep(2)
    text.speak("Hi this is Netra")
    time.sleep(1)
    text.speak("Accessing your front camera")
    time.sleep(1)
    text.speak("Scanning via camera thus results")
    
    while True:
        
        lmlist = []
        success,img = cap.read()
        img = face.findfaces(img,draw=False)
        
        lmlist = face.findfacelm(img,draw=False)
        cv2.imshow("Success",img)
         
        cv2.waitKey(10)
        if(len(lmlist)!=0):
            distance=dis.finddistance(lmlist)
            text.speak("A person is " + str(int(distance)) + " centimeters from you " )
            
        else:
            text.speak("No one in front of you")
            break
    text.speak("I am just a demo right now ")
    text.speak("I will be updated for further versions in comming days by my developers")
    text.speak("Yours Truly Nethra")

main()