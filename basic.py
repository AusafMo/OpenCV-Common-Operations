import cv2 as cv

# # Reading Images
img = cv.imread('kenny.png')
cv.imshow('original image', img)

# Converting to GreyScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
# Canny Edge Detection
# canny = cv.Canny(cv.GaussianBlur(cv.imread('ss.png'), (7,7), cv.BORDER_DEFAULT), 125, 175)
canny = cv.Canny(img, 125, 175)

# cv.imshow('Kenny.....!!!!!! Edge ', canny)

# Dilate Image
canny = cv.Canny(cv.imread('kenny.png'), 125, 175)
dilated = cv.dilate(canny, (3,3), iterations=3)
# cv.imshow('Dilated', dilated)

# Eroded
eroded = cv.erode(dilated, (3,3), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize 
resized = cv.resize(cv.imread('kenny.png'),(700, 500))
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)