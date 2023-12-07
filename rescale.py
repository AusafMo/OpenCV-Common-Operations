import cv2 as cv

def rescaleFrame(frame, scale = 0.75):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]* scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#  Reading Images
img = cv.imread('kenny.png')
cv.imshow('image', img)

resized_img = rescaleFrame(img)
cv.imshow('resized image', resized_img)


# Reading Videos
capture = cv.VideoCapture('kenny.mp4')

# Using Capute set, only for live video
def changeRes(width, height):
   capture.set(3, width)
   capture.set(4, height)

while True :
  isTrue, frame = capture.read()
  
  frame_resized = rescaleFrame(frame)

  cv.imshow('video',frame)
  cv.imshow('Video Resized', frame_resized)

  if cv.waitKey(20) & 0xFF == ord('q'):
    break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)