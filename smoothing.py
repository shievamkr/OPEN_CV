import cv2 as cv
import numpy as np

img = cv.imread('photos/2.jpeg')
cv.imshow('image',img)

# Averaging 
average = cv.blur(img,(3,3))
cv.imshow('average',average)

# GuassianBlur
gauss =cv.GaussianBlur(img,(3,3),0)
cv.imshow('gaussian blur',gauss)

# median blur
median = cv.medianBlur(img,3)
cv.imshow('median blur',median) 

# BIlateral BLUring
bilateral = cv.bilateralFilter(img,5,35,25)
cv.imshow('bilateral blur',bilateral)
#very important
cv.waitKey(0)