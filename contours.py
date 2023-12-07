import cv2 as cv
import numpy as np

# # Reading Images
img = cv.imread('kenny.png')
cv.imshow('image', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', grey)

# blur = cv.GaussianBlur(grey,(5,5), cv.BORDER_DEFAULT )
# cv.imshow('Blurrr!', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny!!!!!!!!!', canny)

# ret, thresh = cv.threshold(grey, 125, 125, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours( canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE )
print(f'{len(contours)} contour(s) found !')
# cv.imshow('Contours', contours)

cv.drawContours(blank, contours, -1, (0, 255, 255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)