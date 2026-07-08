from data import students_data, faculty_data
def student_registration():
    name = input("Enter Student name: ")
    age = int(input("Enter Student age: "))
    gender = input("Enter Student gender: ")
    course = input("Enter Student course: ")
    email = input("Enter Student email: ")
    phone = input("Enter Student phone number: ")
    student = {
        "name": name,
        "age": age,
        "gender": gender,
        "course": course,
        "email": email,
        "phone": phone
    }
    return student

def faculty_registration():
    name = input("Enter Faculty name: ")
    age = int(input("Enter Faculty age: "))
    gender = input("Enter Faculty gender: ")
    department = input("Enter Faculty department: ")
    experience = int(input("Enter Faculty years of experience: "))
    email = input("Enter Faculty email: ")
    phone = input("Enter Faculty phone number: ")
    faculty = {
        "name": name,
        "age": age,
        "gender": gender,
        "department": department,
        "experience": experience,
        "email": email,
        "phone": phone
    }
    return faculty

