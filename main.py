import json
from file_manager import load_users, authenticate, load_students, save_students
from student import Student
import os

students = load_students()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("="*50)
    print(f"{title:^50}")
    print("="*50)

def login():
    users = load_users()
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")
    user = authenticate(username, password, users)
    if user:
        print(f"Login successful! Welcome, {username}.")
        return user
    else:
        print("Invalid credentials.")
        return None

def add_student():
    clear()
    print_header("Add New Student")
    sid = input("Student ID: ")
    if sid in students:
        print("Student already exists!")
        return
    name = input("Name: ")
    students[sid] = Student(sid, name)
    
    # NEW CODE: Create a user account for the student
    create_account = input("Create login account for this student? (y/n): ").lower()
    if create_account == 'y':
        username = input("Enter username for the student: ")
        password = input("Enter password for the student: ")
        
        # Load existing users
        users = load_users()
        # Add new user
        users.append({
            "username": username,
            "password": password,
            "role": "student",
            "student_id": sid  # Link to the student ID
        })
        # Save updated users to user.json
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
        print("Student account created successfully.")

def add_marks():
    clear()
    print_header("Input Student's Marks")
    sid = input("Student ID: ")
    if sid in students:
        subject = input("Subject: ")
        try:
            score = float(input("Marks out of 100 : "))
            students[sid].add_mark(subject, score)
            print("Marks added.")
        except ValueError:
            print("Invalid score.")
    else:
        print("Student not found.")

def view_student():
    clear()
    print_header("View Student Details")
    sid = input("Student ID: ")
    if sid in students:
        s = students[sid]
        print(f"Name: {s.name}")
        print(f"ID: {s.id}")
        print("Marks:")
        for subject, mark in s.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Average: {s.get_average()}")
        print(f"Grade: {s.get_grade()}")
    else:
        print("Student not found.")

def view_student_by_id(sid):
    clear()
    print_header("Student Details")
    if sid in students:
        s = students[sid]
        print(f"Name: {s.name}")
        print(f"ID: {s.id}")
        print("Marks:")
        for subject, mark in s.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Average: {s.get_average()}")
        print(f"Grade: {s.get_grade()}")
    else:
        print("Student not found.")

def view_all():
    clear()
    print_header("All Students")
    print(f"{'ID':<10}{'Name':<20}{'Avg':<10}{'Grade':<10}")
    print("-"*50)
    for s in students.values():
        print(f"{s.id:<10}{s.name:<20}{s.get_average():<10}{s.get_grade():<10}")

def search_by_name():
    clear()
    print_header("Search by Name")
    keyword = input("Enter name keyword: ").lower()
    found = False
    for s in students.values():
        if keyword in s.name.lower():
            print(f"{s.id} - {s.name} | Avg: {s.get_average()} | Grade: {s.get_grade()}")
            found = True
    if not found:
        print("No student found.")

def save_and_exit():
    save_students(students)
    print("Data saved. Exiting...")

def main_menu(user):
    role = user["role"]
    while True:
        print_header("Student Tracker System")
        if role == "admin":
            print("1. Input Student's Details")
            print("2. Input Student's Marks")
            print("3. View Specific Student's Details")
            print("4. View All Student's Details")
            print("5. Search Student by Name")
            print("6. Save and Exit")
        else:
            print("1. View My Details")
            print("2. Exit")

        choice = input("Select an option: ")

        if role == "admin":
            if choice == '1':
                add_student()
            elif choice == '2':
                add_marks()
            elif choice == '3':
                view_student()
            elif choice == '4':
                view_all()
            elif choice == '5':
                search_by_name()
            elif choice == '6':
                save_and_exit()
                break
        else:
            if choice == '1':
                view_student_by_id(user["student_id"])
            elif choice == '2':
                break
        input("\nPress Enter to continue...")

user = login()
if user:
    main_menu(user)
    