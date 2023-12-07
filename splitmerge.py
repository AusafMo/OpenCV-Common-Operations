import cv2 as cv
import numpy as np

img = cv.imread('times.jpg')
cv.imshow('original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# Displaying color channels in color

blue = cv.merge([r, blank, blank])
red = cv.merge([blank, blank, b])
green = cv.merge([blank, g, blank])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging different colors
merged = cv.merge([b, g, r])
cv.imshow('merged', merged)

cv.waitKey(0)