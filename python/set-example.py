import random

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.student_number = random.randint(10000, 99999)
        self.grade = grade

# Create a set containing all high school students
all_students = {
    Student("Alice", 9),
    Student("Tom", 10),
    Student("Charlie", 9),
    Student("David", 11),
    Student("Emma", 12),
    Student("Frank", 9),
    Student("Grace", 10),
    Student("Hannah", 11),
    Student("Isaac", 12),
    Student("Jack", 9),
    Student("Katherine", 10),
    Student("Liam", 11),
    Student("Mia", 12),
    Student("Nathan", 9),
    Student("Olivia", 10),
    Student("Patrick", 11),
    Student("Quincy", 12),
    Student("Rachel", 9),
    Student("Samuel", 10),
    Student("Taylor", 11),
    Student("Uma", 12),
    Student("Victor", 9),
    Student("Wendy", 10),
    Student("Xander", 11),
    Student("Yara", 12),
    Student("Zane", 9),
    Student("Ava", 10),
    Student("Ben", 11),
    Student("Cara", 12),
    Student("Daniel", 9),
    Student("Emily", 10),
    Student("Finn", 11),
    Student("Gemma", 12),
    Student("Henry", 9),
    Student("Ivy", 10),
    Student("Jake", 11),
    Student("Kara", 12),
    Student("Leo", 9),
    Student("Maya", 10),
    Student("Noah", 11),
    Student("Olivia", 12)
}
