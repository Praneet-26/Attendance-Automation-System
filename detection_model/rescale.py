import cv2 as cv
# We should resize and rescle images to reduce computational strain. 
img = cv.imread('detection_model/photos/img1.jpg')
cv.imshow('Person', img)

def rescaleFrame(frame, scale=0.75):
    # works for images, videos and live video.

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1]* scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #Works only for live video.
    capture.set(3,width)
    capture.set(4,height)



img2 = rescaleFrame(img)
cv.imshow('Person_resized', img2)
cv.waitKey(0)
