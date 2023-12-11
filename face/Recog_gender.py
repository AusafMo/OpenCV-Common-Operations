import os
import cv2 as cv
import numpy as np

haar_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml') 

category = ['man', 'woman']
features = np.load('face/features.npy', allow_pickle= True)
labels = np.load('face/true_label.npy', allow_pickle= True)

print("Features and Labels Loaded, reading yml..")
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face/gender_trained.yml')

img = cv.imread('face/woman2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Face', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(label)
    print(f'label = {category[label]} with a confidence of {confidence}.')
    cv.putText(img, str(category[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), thickness = 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255, 0), thickness=2)

cv.imshow('Detected Gender !',img )

cv.waitKey(0)