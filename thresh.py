import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
# cv.imshow('Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)
#simple thresolding 
threshold , thresh =cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

threshold , thresh_inv =cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold',thresh_inv)

#adapted threshold

adaptive_thres=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive  thresholding',adaptive_thres)

adaptive_thres_inv=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('Adaptive  thresholding inv',adaptive_thres_inv)




cv.waitKey(0)