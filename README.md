A Python mini project for managing students, tracking their marks, calculating grades, and managing user login (admin/student) using JSON files for data storage.
✨ Features
1] Login System
2] Admin login
3] Student login linked to their student ID
4] Admin functionalities
5] Add new students
6] Create login accounts for students
7] Input and update student marks
8] View individual student details
9] View all students' performance
10] Search students by name
11] Student functionalities
12] View their own marks, average, and grade
13] Automatic grade calculation based on average marks
14] Data persistence using JSON files (students.json and users.json)
15] Clean console interface with clear menus and organized outputs

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
