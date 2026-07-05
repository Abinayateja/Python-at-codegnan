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

    # elif "attendance" in user_prompt:
    #     attendance()

    # elif "gpa" in user_prompt or "cgpa" in user_prompt:
    #     gpa()

    # elif "marks" in user_prompt or "result" in user_prompt:
    #     marks()

    # elif "calculate" in user_prompt or "calculator" in user_prompt:
    #     calculator()

    # elif "quiz" in user_prompt:
    #     quiz()

    # elif "interview" in user_prompt:
    #     interview_questions()

    elif "motivation" in user_prompt or "motivate" in user_prompt:
        print("AI Assistant: Success is the result of consistent effort. Keep learning!")

    elif "joke" in user_prompt:
        print("AI Assistant: Why do programmers prefer dark mode? Because light attracts bugs!")

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