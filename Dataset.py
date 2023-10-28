import cv2
import numpy as np

# Load the Haar Cascade classifier for detecting faces
face_classifier = cv2.CascadeClassifier('C:/Users/acer/PycharmProject/opencvpython/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return None
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]
        return cropped_face

students = ['pavithra', 'keerthana', 'navya']  # Add names of students
cap = cv2.VideoCapture(0)

for student in students:
    count = 0
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        break

    while count < 100:  # Capture 100 images for each student
        ret, frame = cap.read()
        face = face_extractor(frame)
        if face is not None:
            count += 1

            face = cv2.resize(face, (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            file_name_path = f'C:/Users/acer/Desktop/dataset1/{student}/{count}.jpg'
            cv2.imwrite(file_name_path, face)

            cv2.putText(frame, f'{student}: {count}/100', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', frame)
        else:
            print("Face not found")

        if cv2.waitKey(1) == 13 or count == 100:
            break

cap.release()
cv2.destroyAllWindows()
print('Data set collection completed')
