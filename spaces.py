import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#color spaces --> rgb spaces,grayscal
img = cv.imread('photos/dog.jpg')
cv.imshow('Dog',img)

# plt.imshow(img)
# plt.show()
# point to note --> there is conversion of colour spaces in matplotlib

# BGR to grayscale -->

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

#BGR to HSV -->

hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)
cv.imshow('HSV',hsv)

#BGR to L*A*B
lab =cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

#cann't convert hsv to BGR
# HSV to BGR
hsv_bgr =cv.cvtColor(img,cv.COLOR_HSV2BGR)
cv.imshow('HSV-> BGR',hsv_bgr)

cv.waitKey(0)