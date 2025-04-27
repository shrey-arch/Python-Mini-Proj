A Python mini project for managing students, tracking their marks, calculating grades, and managing user login (admin/student) using JSON files for data storage.
✨ Features
Login System

Admin login

Student login linked to their student ID

Admin functionalities

Add new students

Create login accounts for students

Input and update student marks

View individual student details

View all students' performance

Search students by name

Student functionalities

View their own marks, average, and grade

Automatic grade calculation based on average marks

Data persistence using JSON files (students.json and users.json)

Clean console interface with clear menus and organized outputs

📂 Project Structure
plaintext
Copy
Edit
student_tracker/
│
├── file_manager.py    # Functions to load/save users and students
├── student.py         # Student class handling marks and grades
├── main.py            # (Your current file) Main logic and menu system
├── users.json         # Stores user accounts (admin + students)
└── students.json      # Stores student details and marks
