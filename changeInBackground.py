import numpy as np
import cv2

cap = cv2.VideoCapture(0)

frames = []

for k in range(3):
    ret, crt_frame = cap.read()
    frames.append(cv2.cvtColor(crt_frame,cv2.COLOR_BGR2GRAY))

while(1):
    ret, crt_frame = cap.read()
    del(frames[0])
    frames.append(cv2.cvtColor(crt_frame,cv2.COLOR_BGR2GRAY))
    d1 = cv2.absdiff(frames[0],frames[1])
    d2 = cv2.absdiff(frames[1],frames[2])
    change = cv2.bitwise_and(d1,d2)

    cv2.imshow('frame',change)
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
