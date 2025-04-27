import json
from student import Student

def load_students(filename="students.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            students = {}
            for sid, info in data.items():
                student = Student(sid, info["name"])
                student.marks = info.get("marks", {})  # Load marks from JSON
                students[sid] = student
            return students
    except FileNotFoundError:
        return {}

def save_students(students, filename="students.json"):
    data = {sid: {"name": s.name, "marks": s.marks} for sid, s in students.items()}
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_users(filename="users.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist

def authenticate(username, password, users):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None