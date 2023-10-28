import cv2
import numpy as np
import pandas as pd
from datetime import date, datetime
import create_excel1

# Load the Haar Cascade classifier for detecting faces
face_classifier = cv2.CascadeClassifier('C:/Users/acer/PycharmProject/opencvpython/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        cv2.putText(img, "Unknown", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 0, 0), 2)
        return img, None  # Return None when no face is detected
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
        return img, roi
students = ['pavithra', 'keerthana', 'navya'] #add student names
def get_recognized_student_name(face):
    for (x, y, w, h) in faces:
        face = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
        result = model.predict(face)
        if result[1] < 500:
            confidence = int(100 * (1 - (result[1]) / 300))
            if confidence > 82:
                student_name = students[result[0]]
                mark_attendance(student_name)
                cv2.putText(frame, student_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Implement your face recognition logic here to get the student's name
    return student_name  # Replace with the recognized student's name

model = cv2.face_LBPHFaceRecognizer.create()
model.read('trained_model.yml')  # Load your trained model here

#attendance_data = pd.read_excel('attendance.xlsx', index_col=0)

def mark_attendance(student_name):
    create_excel1.mark_student_present(student_name)
  #  if student_name in attendance_data.columns:
      #  attendance_data.at[0, student_name] = 'Present'



# Main loop for face recognition and attendance marking (similar to your previous code)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame, face = face_detector(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = cv2.resize(gray[y:y + h, x:x + w], (200, 200))
        result = model.predict(face)
        if result[1] < 500:
            confidence = int(100 * (1 - (result[1]) / 300))
            if confidence > 82:
                student_name = get_recognized_student_name(face)  # Replace with actual face recognition
                mark_attendance(student_name)
                current_time = datetime.now().strftime("%H:%M:%S")
                text = f"Student: {student_name}"
                time_text = f"Time: {current_time}"
                cv2.rectangle(frame, (x, y - 30), (x + 200, y), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)
                cv2.putText(frame, time_text, (x, y - 10 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)
            else:
                cv2.putText(frame, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow('Attendance System', frame)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
print('Updated attendance recorded and saved in Excel.')
