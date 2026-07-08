from data import students_data, faculty_data
from chatbot import chatbot
from admin import view_marks, view_attendance, view_profile,calculate_cgpa

def student_login(email, administration_number):

    if administration_number in students_data and students_data[administration_number]["email"] == email:

        print("\n===================================")
        print("Student Login Successful")
        print(f"Welcome {students_data[administration_number]['name']}")
        print("===================================")

        login = True

        while login:

            print("\n========== Student Dashboard ==========")
            print("1. Chat with AI Assistant")
            print("2. View Marks")
            print("3. Calculate CGPA")
            print("4. View Attendance")
            print("5. View Profile")
            print("6. Logout")

            choice = input("Enter Your Choice : ")

            if choice == "1":

                print("\nType 'exit' to return to the dashboard.\n")

                while True:

                    user_prompt = input("You : ")

                    if user_prompt.lower() == "exit":
                        break

                    chatbot(user_prompt)

            elif choice == "2":

                view_marks(administration_number)

            elif choice == "3":

                calculate_cgpa(administration_number)

            elif choice == "4":

                view_attendance(administration_number)

            elif choice == "5":

                view_profile(administration_number)

            elif choice == "6":

                print("Logging Out...")
                login = False

            else:

                print("Invalid Choice. Please select between 1 and 6.")

    else:

        print("Invalid Email or Admission Number.")

def faculty_login(email, faculty_id):
    if faculty_id in faculty_data and faculty_data[faculty_id]["email"] == email:

        print("\nFaculty Login Successful")
        print(f"Welcome {faculty_data[faculty_id]['name']}")

        login = True

        while login:

            print("\n========== Faculty Dashboard ==========")
            print("1. View All Students")
            print("2. View Student Profile")
            print("3. View Student Marks")
            print("4. View Student Attendance")
            print("5. View Student CGPA")
            print("6. View My Profile")
            print("7. Logout")

            choice = input("Enter Your Choice : ")

            if choice == "1":

                print("\n========== Student List ==========\n")

                for student_id, student in students_data.items():

                    print(
                        f"ID : {student_id} | "
                        f"Name : {student['name']} | "
                        f"Course : {student['course']}"
                    )

            elif choice == "2":
                student_id = int(input("Enter Student ID : "))

                if student_id in students_data:

                    view_profile(student_id)

                else:

                    print("Student Not Found")

            elif choice == "3":

                student_id = int(input("Enter Student ID : "))

                if student_id in students_data:

                    view_marks(student_id)

                else:

                    print("Student Not Found")

            elif choice == "4":

                student_id = int(input("Enter Student ID : "))

                if student_id in students_data:

                    view_attendance(student_id)

                else:

                    print("Student Not Found")

            elif choice == "5":

                student_id = int(input("Enter Student ID : "))

                if student_id in students_data:

                    calculate_cgpa(student_id)

                else:

                    print("Student Not Found")

            elif choice == "6":

                print("\n========== Faculty Profile ==========\n")

                faculty = faculty_data[faculty_id]

                print("Faculty ID :", faculty_id)
                print("Name       :", faculty["name"])
                print("Age        :", faculty["age"])
                print("Gender     :", faculty["gender"])
                print("Department :", faculty["department"])
                print("Experience :", faculty["experience"], "Years")
                print("Email      :", faculty["email"])
                print("Phone      :", faculty["phone"])

            elif choice == "7":

                print("Logging Out...")
                login = False

            else:

                print("Invalid Choice")

    else:

        print("Invalid Email or Faculty ID")
