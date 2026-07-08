def chatbot(user_prompt):

    user_prompt = user_prompt.lower()

    if "hi" in user_prompt or "hello" in user_prompt or "hey" in user_prompt:
        print("AI Assistant: Hello! How can I help you today?")

    elif "your name" in user_prompt or "who are you" in user_prompt:
        print("AI Assistant: I am your AI Campus Assistant.")

    elif "help" in user_prompt or "what can you do" in user_prompt:
        print("AI Assistant: I can help with attendance, GPA, marks, quizzes, interview questions, programming concepts and more.")

    elif "python" in user_prompt:
        print("AI Assistant: Python is a high-level programming language developed by Guido van Rossum in 1991.")

    elif "java" in user_prompt:
        print("AI Assistant: Java is an object-oriented programming language.")

    elif "html" in user_prompt:
        print("AI Assistant: HTML is used to create the structure of web pages.")

    elif "css" in user_prompt:
        print("AI Assistant: CSS is used for styling web pages.")

    elif "javascript" in user_prompt:
        print("AI Assistant: JavaScript is used to make web pages interactive.")

    elif "dbms" in user_prompt:
        print("AI Assistant: DBMS stands for Database Management System.")

    elif "sql" in user_prompt:
        print("AI Assistant: SQL is used to communicate with databases.")

    elif "artificial intelligence" in user_prompt or "ai" in user_prompt:
        print("AI Assistant: AI enables computers to perform tasks that normally require human intelligence.")

    elif "machine learning" in user_prompt:
        print("AI Assistant: Machine Learning is a subset of Artificial Intelligence.")

    elif "c language" in user_prompt or "what is c" in user_prompt:
        print("AI Assistant: C is a procedural programming language developed by Dennis Ritchie.")

    elif "c++" in user_prompt:
        print("AI Assistant: C++ is an object-oriented extension of the C programming language.")

    elif "college" in user_prompt or "campus" in user_prompt:
        print("AI Assistant: Welcome to our AI Campus Assistant. I am here to assist students and faculty.")

    elif "faculty" in user_prompt:
        print("AI Assistant: Faculty information is available in the Faculty Dashboard.")

    elif "student" in user_prompt:
        print("AI Assistant: Student information is available in the Student Dashboard.")

    elif "placement" in user_prompt:
        print("AI Assistant: The placement cell helps students prepare for campus interviews.")

    elif "internship" in user_prompt:
        print("AI Assistant: Internships help students gain practical industry experience.")

    elif "project" in user_prompt:
        print("AI Assistant: Choose a project that solves a real-world problem and showcases your skills.")

    elif "interview" in user_prompt:
        print("AI Assistant: Practice technical concepts, coding, aptitude, and communication skills for interviews.")

    elif "resume" in user_prompt:
        print("AI Assistant: A good resume should include education, skills, projects, certifications and achievements.")

    elif "library" in user_prompt:
        print("AI Assistant: The library is open from 9 AM to 5 PM.")

    elif "exam" in user_prompt:
        print("AI Assistant: Please contact the examination branch for the latest exam schedule.")

    elif "attendance" in user_prompt:
        print("AI Assistant: Please use the 'View Attendance' option from the Student Dashboard.")

    elif "marks" in user_prompt or "result" in user_prompt:
        print("AI Assistant: Please use the 'View Marks' option from the Student Dashboard.")

    elif "cgpa" in user_prompt or "gpa" in user_prompt:
        print("AI Assistant: Please use the 'Calculate CGPA' option from the Student Dashboard.")

    elif "profile" in user_prompt:
        print("AI Assistant: Please use the 'View Profile' option from the Student Dashboard.")

    elif "motivation" in user_prompt or "motivate" in user_prompt:
        print("AI Assistant: Success is the result of consistent effort. Keep learning!")

    elif "joke" in user_prompt:
        print("AI Assistant: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "developer" in user_prompt:
        print("AI Assistant: I was developed using Python as an academic project.")

    elif "password" in user_prompt:
        print("AI Assistant: Please contact the administrator if you forgot your password.")

    elif "email" in user_prompt:
        print("AI Assistant: Please contact the administration office for email-related issues.")

    elif "phone" in user_prompt or "contact" in user_prompt:
        print("AI Assistant: Please contact the college administration for assistance.")

    elif "time" in user_prompt:
        print("AI Assistant: This feature is under development.")

    elif "date" in user_prompt:
        print("AI Assistant: This feature is under development.")

    elif "thank" in user_prompt:
        print("AI Assistant: You're welcome!")

    elif "bye" in user_prompt or "exit" in user_prompt:
        print("AI Assistant: Goodbye! Have a great day.")

    else:
        print("AI Assistant: Sorry, I couldn't understand your question.")