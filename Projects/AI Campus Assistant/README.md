# AI Campus Assistant

A menu-driven Python Fundamentals project that simulates a college
management system with role-based access. The project demonstrates
functions, modules, nested dictionaries, authentication, and an AI-style
rule-based chatbot.

------------------------------------------------------------------------

# Project Overview

The system contains three user roles:

-   Student
-   Faculty
-   Admin

Each role has its own dashboard and can access only the features
assigned to it.

The application is divided into multiple Python modules.

    AI Campus Assistant/
    │
    ├── app.py
    ├── login.py
    ├── admin.py
    ├── register.py
    ├── chatbot.py
    ├── data.py
    └── README.md

------------------------------------------------------------------------

# Current Functionalities

## Student

Authentication - Student Login - Student Registration

Dashboard - Chat with AI Assistant - View Semester-wise Marks -
Calculate CGPA - View Semester-wise Attendance - View Profile - Logout

AI Assistant - Answers Python, Java, HTML, CSS, JavaScript - DBMS and
SQL basics - AI and Machine Learning - Interview tips - Motivation -
Jokes - College-related questions

------------------------------------------------------------------------

## Faculty

Authentication - Faculty Login - Faculty Registration

Dashboard - View All Students - View Student Profile - View Student
Marks - View Student Attendance - View Student CGPA - View My Profile -
Logout

------------------------------------------------------------------------

## Admin

Authentication - Admin Login

Dashboard - Add Student - Add Faculty - View Students - View Faculty -
Logout

------------------------------------------------------------------------

# Data Storage

The project currently stores information using nested dictionaries.

Main datasets include: - students_data - faculty_data - marks_data -
attendance_data

Marks are stored semester-wise.

Example

``` python
marks_data = {
    1001: {
        "Semester 1": {
            "Programming in C": 88,
            "Mathematics": 91
        }
    }
}
```

Attendance is also stored semester-wise.

------------------------------------------------------------------------

# Project Modules

## app.py

Entry point

Responsibilities - Main menu - Navigation - Calls login functions

------------------------------------------------------------------------

## login.py

Responsibilities

-   Student Login
-   Faculty Login
-   Student Dashboard
-   Faculty Dashboard

------------------------------------------------------------------------

## admin.py

Responsibilities

-   Admin Login
-   Student Management
-   Faculty Management
-   View Marks
-   View Attendance
-   Calculate CGPA
-   View Profiles

------------------------------------------------------------------------

## chatbot.py

Contains the AI Assistant logic using conditional statements.

------------------------------------------------------------------------

## register.py

Handles student and faculty registration.

------------------------------------------------------------------------

## data.py

Stores all project data using nested dictionaries.

------------------------------------------------------------------------

# How the Application Works

    Main Menu
        │
        ├── Student
        │      │
        │      ├── Login
        │      ├── Dashboard
        │      ├── Chatbot
        │      ├── Marks
        │      ├── Attendance
        │      ├── CGPA
        │      └── Profile
        │
        ├── Faculty
        │      │
        │      ├── Login
        │      ├── Student Details
        │      ├── Marks
        │      ├── Attendance
        │      └── Profile
        │
        └── Admin
               │
               ├── Login
               ├── Add Student
               ├── Add Faculty
               ├── View Students
               └── View Faculty

------------------------------------------------------------------------

# Future Enhancements (OOP + JSON Version)

The next version can include:

-   Object-Oriented Programming
-   JSON-based persistent storage
-   Password management
-   Search by ID or Email
-   Edit Student Information
-   Edit Faculty Information
-   Delete Records
-   Chat History
-   Timetable Management
-   Notifications
-   Assignment Tracking
-   Placement Module
-   Fee Management
-   Examination Module
-   Results Export
-   GPA Analytics

------------------------------------------------------------------------

# OOP Design (Next Version)

                    Person
                       │
            ┌──────────┴──────────┐
            │                     │
         Student              Faculty
            │
          Admin

Concepts to demonstrate

-   Classes and Objects
-   Constructors
-   Inheritance
-   Encapsulation
-   Polymorphism
-   Abstraction
-   File Handling
-   JSON Persistence

------------------------------------------------------------------------

# Technologies Used

-   Python
-   Functions
-   Modules
-   Nested Dictionaries
-   Conditional Statements
-   Loops
-   Menu-driven Programming

------------------------------------------------------------------------

# Learning Outcomes

This project demonstrates:

-   Modular programming
-   Function design
-   Dictionary manipulation
-   Nested dictionary traversal
-   Authentication
-   Role-based access
-   Menu-driven applications
-   Basic chatbot implementation
-   CGPA calculation
-   Attendance tracking
-   Marks management

------------------------------------------------------------------------

# Author

Abinay Teja Gaddam

Computer Science and Engineering
