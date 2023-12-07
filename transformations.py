import cv2 as cv
import numpy as np
img = cv.imread('ausaf.png')

# cv.imshow('original image', img)


# Translations

def translate(img, x, y):

    # -x --> left, -y --> up
    # x --> right, y --> down
    
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 100)
cv.imshow('translated', translated)

# Rotation
def rotate( img, angle, rotPoint = None):
    
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -90)
cv.imshow('rotated', rotated)

# resizing
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)


# Flipping
flip = cv.flip(img, 1)
cv.imshow('Flipped', flip)

# Cropping 
cropped = img[200:400, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)