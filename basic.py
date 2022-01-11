import  cv2 as cv

img = cv.imread('photos/dog.jpg')
cv.imshow('img',img)

#converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

#blur an image 
blur =cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#Edge Cascade 
edge= cv.Canny(blur,125,175)
# cv.imshow('Canny',edge)

#Dialating the image
dilated =cv.dilate(edge,(11,11),iterations=1)
# cv.imshow('Dilated',dilated)

#eroding 
eroded = cv.erode(dilated,(3,3),iterations=2)
# cv.imshow('Eroded',eroded)

#Resize
# resized = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping
cropped = resized[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)