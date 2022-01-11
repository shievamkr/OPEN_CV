import cv2 as cv

#Reading images
img = cv.imread('photos/1.jpg') #reading data

cv.imshow('img', img) #diplaying data

cap=cv.VideoCapture(0) # camera capture

def rescaleframe(frame,scale=0.75):
    # it will work for images videos and live videos 
    width = int(frame.shape[1] * scale)
    lenght = int(frame.shape[0] * scale)
     
    dimension =(width,lenght)
    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #only work for live video
    cap.set(3,width)
    cap.set(4,height)
    

resized_image = rescaleframe(img)
cv.imshow('image_resized', resized_image)

#reading videos

cap = cv.VideoCapture('videos/v1.mp4') 

while True:
    isTrue, frame =cap.read()
    
    frame_resized =rescaleframe(frame,scale=0.2)
    
    cv.imshow('video_resized',frame_resized)
    cv.imshow('video',frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
cap.release()
cv.destroyAllWindows()


# cv.waitKey(0) #waiting for key press
