import cv2
import numpy as np
from os import listdir, makedirs
from os.path import isfile, join

data_path = 'C:/Users/acer/Desktop/dataset1/'
students = ['pavithra', 'keerthana', 'navya']  # Add names of students
Training_Data, Labels = [], []

# Create directories if they don't exist
for student in students:
    student_path = data_path + student
    makedirs(student_path, exist_ok=True)  # Create the directory if it doesn't exist

for student in students:
    student_images = [f for f in listdir(data_path + student) if isfile(join(data_path + student, f))]

    for i, file in enumerate(student_images):
        image_path = data_path + student + '/' + student_images[i]
        try:
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if image is not None:
                # Resize the image to a consistent size (e.g., 200x200 pixels)
                image = cv2.resize(image, (200, 200))
                Training_Data.append(np.asarray(image, dtype=np.uint8))
                Labels.append(students.index(student))
            else:
                print(f"Failed to load image: {image_path}")
        except Exception as e:
            print(f"Error processing image: {image_path}")
            print(str(e))

Labels = np.asarray(Labels, dtype=np.int32)
model = cv2.face_LBPHFaceRecognizer.create()
model.train(np.asarray(Training_Data), np.asarray(Labels))
model.save('trained_model.yml')  # Save the trained model
print("Dataset model training completed")
