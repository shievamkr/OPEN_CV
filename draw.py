import  cv2 as cv
import numpy as np

blank =  np.zeros((500,500,3), dtype ='uint8')
cv.imshow('Blank',blank)

#paint the image with certain color values
blank[:]=0,0,255
# cv.imshow('Red',blank)

# Draw a rectangle around
# cv.rectangle(blank,(0,0),(255,255),(0,255,0),thickness=2)
cv.rectangle(blank,(0,0),(255,255),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)

# draw a circle 
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(111,111,255),thickness=-1)
# cv.imshow('circle',blank)

#draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(111,111,255),thickness=4)
# cv.imshow('line',blank)

# write text on a images
cv.putText(blank, "hello shivam", (225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,225,0),2)
cv.imshow('line',blank)

cv.waitKey(0)