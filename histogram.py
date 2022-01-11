import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/model2.jpg')
cv.imshow('image',img)

blank =np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

circle = cv.circle(blank,(img.shape[1]//2-150,img.shape[0]//2-150),100,255,-1)
# cv.imshow('circle',circle)
masked_image = cv.bitwise_and(img,img,mask=circle)
cv.imshow('masked_image',masked_image)

# grayscale to histogram
# gray_hist =cv.calcHist([masked_image],[0], None, [256],[0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel("# of pixels")
# plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.show()

#colour histogram
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)