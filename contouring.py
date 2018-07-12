import cv2
import numpy as np

img = cv2.imread('leave.jpg')
blurred=cv2.pyrMeanShiftFiltering(img,21,51)
gray=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
res , threshold=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th, contours,_=cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print("Contours -> ", len(contours))
cv2.drawContours(threshold,contours,-1,(0,0,255),6)
cv2.imshow('original',threshold)
cv2.waitKey(0)

