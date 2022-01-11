import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
cv.imshow('image',img)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap =np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

#sobel gradient
sobel_x=cv.Sobel(gray, cv.CV_64F,1,0)
sobel_y=cv.Sobel(gray, cv.CV_64F,0,1)
sobel_mix =cv.bitwise_and(sobel_x,sobel_y)
cv.imshow('sabol_mix',sobel_mix)

cv.imshow('sobel Y',sobel_x)
cv.imshow('sobel X',sobel_y)

cv.waitKey(0)