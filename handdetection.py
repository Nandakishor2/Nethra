import mediapipe as mp
import cv2
cap = cv2.VideoCapture(1)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils
while True:
    success,img = cap.read()
    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgrgb)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,handlms,mphands.HAND_CONNECTIONS)

    cv2.imshow("Image",img) 
    cv2.waitKey(1)