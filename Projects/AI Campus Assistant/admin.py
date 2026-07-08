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

        print("-" * 70)
        print(f"Admission No : {admin_no}")
        print(f"Name         : {student['name']}")
        print(f"Age          : {student['age']}")
        print(f"Gender       : {student['gender']}")
        print(f"Course       : {student['course']}")
        print(f"Email        : {student['email']}")
        print(f"Phone        : {student['phone']}")
        print("-" * 70)

def view_faculty(faculty_list):
    for faculty_id, faculty in faculty_list.items():

        print("-" * 70)
        print(f"Faculty ID   : {faculty_id}")
        print(f"Name         : {faculty['name']}")
        print(f"Age          : {faculty['age']}")
        print(f"Gender       : {faculty['gender']}")
        print(f"Department   : {faculty['department']}")
        print(f"Experience   : {faculty['experience']} Years")
        print(f"Email        : {faculty['email']}")
        print(f"Phone        : {faculty['phone']}")
        print("-" * 70)

def view_marks(administration_number):

    if administration_number not in students_data:
        print("Student not found.")
        return

    semester = input("Enter Semester Number (1-8): ")

    semester_name = f"Semester {semester}"

    if semester_name not in marks_data[administration_number]:
        print("Invalid Semester.")
        return

    print("\n====================================")
    print(f"{semester_name} Marks")
    print("====================================")

    total = 0

    for subject, marks in marks_data[administration_number][semester_name].items():

        print(f"{subject:<30} : {marks}")

        total += marks

    average = total / len(marks_data[administration_number][semester_name])

    print("------------------------------------")
    print("Total Marks :", total)
    print("Average     :", round(average,2))

def view_attendance(administration_number):

    if administration_number not in students_data:
        print("Student not found.")
        return

    semester = input("Enter Semester Number (1-8): ")

    semester_name = f"Semester {semester}"

    if semester_name not in attendance_data[administration_number]:
        print("Invalid Semester.")
        return

    print("\n====================================")
    print("Attendance Report")
    print("====================================")

    print("Semester   :", semester_name)
    print("Attendance :", attendance_data[administration_number][semester_name],"%")

def view_profile(administration_number):

    if administration_number not in students_data:
        print("Student not found.")
        return

    student = students_data[administration_number]

    print("\n========== Student Profile ==========")

    print("Admission No :", administration_number)
    print("Name         :", student["name"])
    print("Age          :", student["age"])
    print("Gender       :", student["gender"])
    print("Course       :", student["course"])
    print("Email        :", student["email"])
    print("Phone        :", student["phone"])


def calculate_cgpa(administration_number):

    if administration_number not in students_data:
        print("Student not found.")
        return

    total_gpa = 0
    semesters = 0

    print("\n=========== GPA Report ===========")

    for semester, subjects in marks_data[administration_number].items():

        total = sum(subjects.values())

        average = total / len(subjects)

        if average >= 90:
            gpa = 10
        elif average >= 80:
            gpa = 9
        elif average >= 70:
            gpa = 8
        elif average >= 60:
            gpa = 7
        elif average >= 50:
            gpa = 6
        else:
            gpa = 0

        print(f"{semester:<15} GPA : {gpa}")

        total_gpa += gpa
        semesters += 1

    cgpa = total_gpa / semesters

    print("----------------------------------")
    print("Overall CGPA :", round(cgpa,2))