
# import the necessary packages
import numpy as np
import argparse
import cv2


image = cv2.VideoCapture("C0520.MP4")


while True:

    ret, frame=image.read()
    cv2.namedWindow("kolorki",0)
    cv2.resizeWindow("kolorki",3000,1000)

    mask=cv2.inRange(    cv2.cvtColor(frame,cv2.COLOR_RGB2HSV),np.array([93,86,192]),np.array([120,120,210]))
    cv2.erode(mask,mask,iterations=5)
    cv2.dilate(mask,kernel=None,dst=mask,iterations=5)
    output=cv2.bitwise_and(frame,frame,mask=mask)
    kupa1,kupa2=cv2.findContours(mask, mode=cv2.RETR_CCOMP,method= cv2.CHAIN_APPROX_SIMPLE)
    print(f"x:,{kupa1[0][0][0][0]},y:{kupa1[0][0][0][1]}")
    if kupa1[0][0][0][0]>400:
        cv2.rectangle(frame,(kupa1[0][0][0][0]-80,kupa1[0][0][0][1]-60),(kupa1[0][0][0][0]+50,kupa1[0][0][0][1]+20),(0,0,0),5)
    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break

    cv2.imshow("kolorki",np.hstack([frame,output]))
