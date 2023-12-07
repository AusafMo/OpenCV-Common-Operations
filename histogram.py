import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Reading Images
img = cv.imread('times.jpg')
cv.imshow('image', img)

# Greyscale it
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Making a mask
circle = cv.circle(np.zeros(img.shape[:2], dtype = 'uint8'), (img.shape[1]//2 + 250 , img.shape[0]//2 + 250), 200, 255, -1)
cv.imshow('Mask', circle)

masked = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow('Mask', masked)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# color histograms
colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], masked, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)