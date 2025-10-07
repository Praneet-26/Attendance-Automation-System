import os
import cv2 as cv
import numpy as np

persons = ["Shreya", "Praneet"]

DIR = r"/Users/praneetnaik/Desktop/Attendance-Automation-System/detection_model/train"

p = []

haar_cascade = cv.CascadeClassifier('detection_model/classifier/haar_face.xml')

features = []
labels = []

def train_image():
    for person in persons:
        path = os.path.join(DIR, person)
        label = persons.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                face_roi = cv.resize(faces_roi, (200, 200))
                features.append(faces_roi)
                labels.append(label)

train_image()
print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)