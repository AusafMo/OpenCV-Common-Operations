import cv2 as cv
import numpy as np

img = cv.imread('kenny.png')
cv.imshow('Orginal', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

# Laplacian Edge Detection
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobel_dx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_dy = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_dx, sobel_dy)

cv.imshow('gradient dX', sobel_dx)
cv.imshow('gradient dY', sobel_dy)
cv.imshow('Combined Sobel', combined_sobel)

# Comparison with Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)