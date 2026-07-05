from data import students_data, faculty_data
from chatbot import chatbot
from admin import view_marks, view_attendance, view_profile

def student_login(email, administration_number):
    if administration_number in students_data and students_data[administration_number]["email"] == email:
        print("Student login successful.")
        login = True
        while login:
            print("1. Chat with AI Assistant \n2. View Marks \n3. Calculate CGPA \n4. View Attendance \n5. View Profile \n6. Logout")
            choice = input("Please select an option: ")
            if choice == "1":
                exit = False
                while not exit:
                    user_prompt = input("You: ")
                    if user_prompt.lower() == "exit":
                        exit = True
                    else:
                        chatbot(user_prompt)
            elif choice == "2":
                # View Marks
                marks = view_marks(administration_number)
                print(f"Marks for {students_data[administration_number]['name']}: {marks}")

            elif choice == "3":
                # Calculate CGPA
                # # cgpa = calculate_cgpa(administration_number)
                # print(f"CGPA for {students_data[administration_number]['name']}: {cgpa}")
                pass  # Placeholder for CGPA calculation functionality

            elif choice == "4":
                # View Attendance
                attendance = view_attendance(administration_number)
                print(f"Attendance for {students_data[administration_number]['name']}: {attendance}")

            elif choice == "5":
                # View Profile
                view_profile(administration_number)

            elif choice == "6":
                login = False
                print("Logging out...")
                print("Student logged out.")

            else:
                print("Invalid selection. Please try again.")

def faculty_login(email, faculty_id):
    if faculty_id in faculty_data and faculty_data[faculty_id]["email"] == email:
        print("Faculty login successful.")
        print("Welcome, " + faculty_data[faculty_id]["name"] + "!")
