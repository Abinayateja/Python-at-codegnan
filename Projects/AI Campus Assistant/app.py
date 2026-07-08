from register import student_registration, faculty_registration
from login import student_login, faculty_login
from admin import admin_login
from data import students_data,faculty_data
from admin import add_student, add_faculty

# main
if __name__ == "__main__":
    exit = False
    while(exit == False):
        print("Welcome to AI Campus Assistant")
        print("1. Student Register \n2. Student Login \n3. Faculty Register \n4. Faculty Login \n5. Admin Login \n6. Exit")
        choice = input("Please select an option: ")
        
        if choice == "1":
            add_student(students_data)

        elif choice == "2":
            email = input("Enter your email: ")
            administration_number = int(input("Enter your administration number: "))
            student_login(email, administration_number)

        elif choice == "3":
            add_faculty(faculty_data)

        elif choice == "4":
            email = input("Enter your email: ")
            faculty_id = int(input("Enter your faculty ID: "))
            faculty_login(email, faculty_id)

        elif choice == "5":
            password = input("Enter admin password: ")
            admin_login(password)

        elif choice == "6":
            print("Thank you for using AI Campus Assistant.")
            print("See You Soon!")
            exit = True

        else:
            print("Invalid selection. Please try again.")