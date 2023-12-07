import cv2 as cv

img = cv.imread('times.jpg')
cv.imshow('Orginal', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)


cv.waitKey(0)