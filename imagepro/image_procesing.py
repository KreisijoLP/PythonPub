import cv2
import os
import time
import numpy as np

cap = cv2.VideoCapture(0);

if not cap.isOpened():
    raise IOError("Error")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    cv2.putText(frame, "Test", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.rectangle(frame, (100, 100), (200, 200), (255, 255, 255))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Input', frame)
    cv2.imshow('Gray', gray)

    sumwhite = np.sum(gray == 255)
    sumblack = np.sum(gray == 0)
    print("White "+str(sumwhite))
    print("Black: "+str(sumblack))

    #print("#########"+str(frame)+"##########")
    c = cv2.waitKey(1)
    if c == 27:
        break


cap.release()
cv2.destroyAllWindows()