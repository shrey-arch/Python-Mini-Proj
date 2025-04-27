class Student:
    def __init__(self, sid, name):
        self.id = sid
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def get_average(self):
        if not self.marks:
            return 0
        return round(sum(self.marks.values()) / len(self.marks), 2)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 40:
            return 'D'
        else:
            return 'F'
