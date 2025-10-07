
import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('detection_model/classifier/haar_face.xml')

people = ["Shreya", "Praneet"]
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'detection_model/train/group1.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    faces_roi = cv.resize(faces_roi, (200, 200))  # match training size

    label, confidence = face_recognizer.predict(faces_roi)

    # Set a confidence threshold to handle unknown faces
    if confidence < 100:
        name = people[label]
    else:
        name = "Unknown"

    # Draw rectangle and put name above it
    cv.putText(img, f"{name} ({int(confidence)})", (x, y-10),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Detected Faces", img)
cv.waitKey(0)
cv.destroyAllWindows()