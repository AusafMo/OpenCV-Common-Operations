import cv2 as cv

# # Reading Images
# img = cv.imread('ss.png')
# cv.imshow('image', img)


# Reading Videos
capture = cv.VideoCapture('kenny.mp4')

while True :
  isTrue, frame = capture.read()
  cv.imshow('video',frame)

  if cv.waitKey(20) & 0xFF == ord('q'):
    break

capture.realease()
cv.waitKey(0)