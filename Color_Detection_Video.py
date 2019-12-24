import numpy as np
import cv2
import imutils

o = []
cap = cv2.VideoCapture("1.mp4")
numframes = cap.get(7)
count=0
while(count < numframes):
    count += 1
    _, frame = cap.read()
    image = imutils.resize(frame, width=900)
    lower_red = np.array([0,0,120], dtype = "uint8")
    upper_red = np.array([100,100,255], dtype = "uint8")
    kernel = np.ones((20,20), np.uint16)
    mask = cv2.inRange(image, lower_red, upper_red)
    output1 = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    output = cv2.bitwise_and(image, image, mask = mask)
    cnts = cv2.findContours(output1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)

    o.append((x, y))

    cv2.imshow('Output', np.hstack([output, image]))
    cv2.waitKey(30)

cv2.destroyAllWindows()
cap.release()
