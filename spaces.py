import cv2 as cv

# Reading Images
img = cv.imread('kenny.png')
cv.imshow('image', img)

# BGR to GREY
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# BGR to HSV HueSaturationValue
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

cv.waitKey(0)