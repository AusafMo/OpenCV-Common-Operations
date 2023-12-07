import cv2 as cv
import numpy as np

blank = np.zeros((600,600, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('kenny.png')
# cv.imshow('Image', img)

# 1. Paint Image with a color

# blank[:] = 0, 255, 0
# blank[200:300, 300:400] = 0, 0, 255

# # 2. Draw a Rectangle
# # cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness= 4)
# cv.rectangle(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness= cv.FILLED)

# # 3. Draw a Circle
# cv.circle(blank,(blank.shape[0]//2, blank.shape[1]//2), 40, (0, 142, 255), thickness = 3)

# # 4. Draw a Line
# cv.line(blank, (100, 250),(300, 400), (255, 255, 255), thickness = 3)
# cv.imshow('Green', blank)

# 5. Wrire text
cv.putText(blank, "It is Kenny 0_0 !", (26, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2 )
cv.imshow('Text', blank)

cv.waitKey(0)