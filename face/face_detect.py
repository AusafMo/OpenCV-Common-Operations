import cv2 as cv

img = cv.imread('face/levi.jpg')
cv.imshow('Levi', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Colorless Levi!!!!', gray)

#  What parameters mean in face_detect.py's haar_cascade.detecMultiscale() method : 
#  https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters

# Download .xml file from the GitHub repo of OpenCV
# haar_cascade = cv.CascadeClassifier('face/har_face.xml')
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# Alternatively, dont need haarcascade_~~~~.xml files this way
haar_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml') 
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.5, minNeighbors = 1)

# The faces_rect is a list of coordinates over the faces, so you can draw over it
for (x, y, w, h) in faces_rect :
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness = 2)
cv.imshow('Detected Levi Face, boy he is annoyed', img)

print(f'The number of faces detected : {len(faces_rect)}')

# MULTIFACES DETECTION
group = cv.imread('face/scouts.jpg')
cv.imshow('Dattabayo!', group)

group_gray = cv.cvtColor(group, cv.COLOR_BGR2GRAY)
cv.imshow('Grey Dattabayo !', group_gray)

faces_rect = haar_cascade.detectMultiScale(group_gray, scaleFactor= 1.1, minNeighbors = 3)
cv.imshow('Face of Scouts ?', group)

for (x, y, w, h) in faces_rect :
    cv.rectangle(group, (x,y), (x+w, y+h), (0, 255, 0), thickness = 2)
cv.imshow('Detected faces', group)

print(f'The number of faces detected : {len(faces_rect)}')

cv.waitKey(0)