import numpy as np
import cv2

image = cv2.imread('/home/mohammadreza/Documents/Code/Python/Color_Detection/Image.jpg')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([22, 93, 0], dtype="uint8")
upper = np.array([45, 255, 255], dtype="uint8")
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow('Window', np.hstack([original, output]))
cv2.waitKey()
