import cv2 as cv



img = cv.imread('detection_model/photos/img1.jpg')
print(img)

cv.imshow('Person', img)

def rescaleFrame(frame, scale=0.75):

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1]* scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img2 = rescaleFrame(img)
cv.imshow('Person_resized', img2)
cv.waitKey(0)

# capture = cv.VideoCapture(0)

# while True:
#     isTrue , frame = capture.read() #Grabbing the video frame by frame
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) or 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()