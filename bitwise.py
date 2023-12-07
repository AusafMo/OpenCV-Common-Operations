import cv2 as cv
import numpy as np

img = cv.imread('times.jpg')
cv.imshow('original', img)

blank = np.zeros((500,500), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (50,50), (450,450), 255, -1)
circle = cv.circle(blank.copy(), (250, 250), 250, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwise_xor)


# bitwise XOR
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwise_not)

cv.waitKey(0)