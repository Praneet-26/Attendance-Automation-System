import cv2 as cv
import numpy as np
  

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)


#Paint the blank with a certain color

blank[200:300, 400:500] = 0,0,255
cv.imshow("Color", blank)

# Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0),thickness=-1)
cv.imshow("Rectangle",blank)

#Draw a Circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=-1)
cv.imshow("Circle",blank)

#Draw a line
cv.line(blank, (0,0),(255,255), (255,100,255),thickness=3)
cv.imshow("Line",blank)

#Write a text
cv.putText(blank,"Hi am the Best", (100,355),cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)
