import cv2 as cv

#Reading images
# img = cv.imread('photos/1.jpg') #reading data

# cv.imshow('img', img) #diplaying data

# cap=cv.VideoCapture(0) # camera capture

#reading videos

cap = cv.VideoCapture('videos/v1.mp4') 

while True:
    isTrue, frame =cap.read()
    
    cv.imshow('video',frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
cap.release()
cv.destroyAllWindows()


# cv.waitKey(0) #waiting for key press
