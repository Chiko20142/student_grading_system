print("STUDENT GRADING SYSTEM")


students = [
    {"name": "Chiko", "mark": 85},
    {"name": "Jason", "mark": 90},
    {"name": "Michael", "mark": 70},
    {"name": "Wilson", "mark": 79},
    {"name": "ELeman", "mark": 87},
    {"name": "Emmanuel", "mark":85},
    {"name": "Joseph", "mark":62},
    {"name": "Justin", "mark":44}
    ]

def grading_system(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "Fail"

for student in students:
    grade = grading_system(student["mark"])
    print("Name:",student["name"],"|Mark:", student["mark"],"|Grade:", grade)
    

