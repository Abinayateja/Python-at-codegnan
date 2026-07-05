from register import student_registration, faculty_registration
from data import students_data,marks_data,attendance_data, faculty_data

def admin_login(password):
    if password == "admin123":
        login = True
        print("Admin login successful.")
        while login:
            print("1. Add Student \n2. Add Faculty \n3. View Students \n4. View Faculty \n5. Logout")
            choice = input("Please select an option: ")
            if choice == "1":
                add_student(students_data)
            elif choice == "2":
                add_faculty(faculty_data)
            elif choice == "3":
                view_students(students_data)
            elif choice == "4":
                view_faculty(faculty_data)
            elif choice == "5":
                login = False
                print("Logging out...")
                print("Admin logged out.")


def add_student(student_list):
    count = len(student_list) + 1001
    student = student_registration()
    student_list.setdefault(count, student)
    print(f"Student added with administration number: {count}")

def add_faculty(faculty_list):
    count = len(faculty_list) + 101
    faculty = faculty_registration()
    faculty_list.setdefault(count, faculty)
    print(f"Faculty added with ID: {count}")

def view_students(student_list):
    for admin_no, student in student_list.items():
        print(f"ID: {admin_no}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Gender: {student['gender']}")
        print(f"Course: {student['course']}")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone']}")

def view_faculty(faculty_list):
    for faculty_id, faculty in faculty_list.items():
        print(f"ID: {faculty_id}")
        print(f"Name: {faculty['name']}")
        print(f"Age: {faculty['age']}")
        print(f"Gender: {faculty['gender']}")
        print(f"Department: {faculty['department']}")
        print(f"Email: {faculty['email']}")
        print(f"Phone: {faculty['phone']}")

def view_marks(administration_number):
    if administration_number in students_data:
        marks = marks_data[administration_number]
        print(f"Marks for {students_data[administration_number]['name']}: {marks}")

def view_attendance(administration_number):
    if administration_number in students_data:
        attendance = attendance_data[administration_number]
        print(f"Attendance for {students_data[administration_number]['name']}: {attendance}")

def view_profile(administration_number):
    if administration_number in students_data:
        profile = students_data[administration_number]
        print(f"Profile for {profile['name']}: Age: {profile['age']}, Gender: {profile['gender']}, Course: {profile['course']}, Email: {profile['email']}, Phone: {profile['phone']}")
        print(f"Marks: {marks_data[administration_number]}, Attendance: {attendance_data[administration_number]}")