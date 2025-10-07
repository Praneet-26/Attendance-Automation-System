import cv2 as cv
img = cv.imread('detection_model/photos/img1.jpg')
cv.imshow('Normal', img)

#Grayscale - Better for running algorithms as there are no RGB colors which makes algos to run faster becuase of less computation.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale', gray)

#Blur- Bluring the image involves reducing the pixels
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Canny Edge Cascade
Canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', Canny)


#Dilated
dilated = cv.dilate(Canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Eroding
erode = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Erode', erode)

#Resizing
Resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', Resize)


#Cropping
crop = img[50:200, 200:400]
cv.imshow('Cropped', crop)

cv.waitKey(0)