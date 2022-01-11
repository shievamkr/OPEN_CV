import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')

cv.imshow('Dog',img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank',blank)

canny =cv.Canny(img,125,175)
cv.imshow('Canny',canny)

ret,thresh = cv.threshold(gray,125,175, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
contours,hierchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) Found! ')

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)