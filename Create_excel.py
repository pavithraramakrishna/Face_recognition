import pandas as pd
from datetime import date

# Define the list of students
students = ['pavithra', 'keerthana', 'navya']

# Get the current date
today = date.today()

# Define the file name to create
file_name = 'C:/Users/acer/Desktop/attendance_' + today.strftime("%Y%m%d") + '.xlsx'

#def create_initial_attendance_sheet():
    # Create an empty dictionary to store attendance data
attendance_data = {'Date': [today.strftime("%Y-%m-%d")]}

# Initialize attendance columns for each student as "Absent"
for student in students:
   attendance_data[student] = ['Absent']

# Create a DataFrame from the dictionary
attendance_df = pd.DataFrame(attendance_data)
file_name = 'C:/Users/acer/Desktop/attendance_' + today.strftime("%Y%m%d") + '.xlsx'

# Save the DataFrame to the Excel file
try:
    attendance_df.to_excel(file_name, index=False)
    print(f"Attendance Excel file '{file_name}' created for today's date.")
except PermissionError:
    print(f"Error:Permission denied.you might not have not write access to the specified directory")
except Exception as e:
    print(f"An error occured:{str(e)}")



def mark_student_present(student_name):
    # Load the existing attendance sheet
    try:
        attendance_df = pd.read_excel(file_name)
    except FileNotFoundError:
        print(f"Error: The attendance file '{file_name}' does not exist.")
        return
    except Exception as e:
        print(f"An error occurred while reading the attendance file: {str(e)}")

    # Check if the student name exists in the attendance sheet
    if student_name in attendance_df.columns:
        # Update the attendance status to 'Present' for the specified student
        attendance_df.at[0, student_name] = 'Present'
        # Save the updated attendance sheet
        try:
            attendance_df.to_excel(file_name, index=False)
            print(f"{student_name} marked as present in the attendance sheet.")
        except PermissionError:
            print(f"Error: Permission denied. You might not have write access to the specified directory.")
        except Exception as e:
            print(f"An error occurred while saving the attendance file: {str(e)}")
    else:
        print(f"Error: Student '{student_name}' not found in the attendance sheet.")
