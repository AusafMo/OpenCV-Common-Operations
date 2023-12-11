import os
import cv2 as cv
import numpy as np 
import time

category = ['man', 'woman']

images = []
dir = 'face/faces'

haar_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml') 
for img in os.listdir(dir):
    images.append(img)

print(images)

feature = []
true_label = []

def train():
    
    total_count = 0
    
    for cat in category:
        cat_count = 0
        path = os.path.join(dir, cat)
        label = cat.index(cat)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

            for (x, y, w, h) in faces_rect:
                
                face_roi = gray[y:y+h, x:x+w]
                feature.append(face_roi)
                true_label.append(label)
            
            cat_count += 1

            total_count += 1
            if total_count % 200 == 0:
                 print(f'Training for features in category {cat}..'+ str(((total_count+1)*100)//2000) +'%  completed.')

            if cat_count > 1000:
                break

        if cat_count > 1000:
            continue

start_time = time.time()
train()
end_time = time.time()
elapsed_time = end_time - start_time

print(f"\n Training for features Done! Yay! --- It took a total of {int(elapsed_time)//60} minutes and {int(elapsed_time)%60} seconds. \n")
print(f"The length of Features:{len(feature)} and the Length of True Labels are : {len(true_label)}. \n")
print("Starting Training for Classifier...")

feature = np.array(feature, dtype='object')
true_label = np.array(true_label)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(feature,true_label)
face_recognizer.save('face/gender_trained.yml')

np.save('face/features.npy', feature)
np.save('face/true_label.npy', true_label)
print("Executed Successfully!")