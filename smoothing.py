import cv2 as cv

img = cv.imread('times.jpg')
cv.imshow('orignal', img)

# Averaging Blur
average = cv.blur(img, (7,7))
cv.imshow('average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral Blurring, preserves edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)