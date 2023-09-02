import random

class Student:
       def __init__(self, first_name, last_name, student_number):
        self.first_name = first_name
        self.last_name = last_name
     
        self.student_number = student_number

        # classes MUST be a list because the classes are grouped in lists
        # according to categories. Lists (and dicts) cannot be set elements.
        self.classes = [None] * 6


def populate_classes(students, classes):


    for student in students:

        # Mixes up the order of class categories for each student
        random.shuffle(classes)
        number = 0

        for category in classes:
                class_assigned = random.choice(category)
                student.classes[number] = class_assigned
                number += 1
     

    
def print_classList(student):
    print(f"\n\nClass Schedule for {student.first_name} {student.last_name}:\n")
    for i, class_name in enumerate(student.classes, start=1):
        print(f"Class {i}: {class_name}")

def is_student(first_name, last_name, student_number, all_students):
    """
    Checks to see if a Student object is in all_students set. HINT: Remember
    that each Student object was fed into the hashing function to determine 
    its hash table location, so an object is going to be needed again to check 
    for membership.
    """
     
    if Student(first_name, last_name, student_number) in all_students:
        print(f"{student.first_name} {student.last_name} is a student.\n")
    else:
        print(f"{student.first_name} {student.last_name} is not a student.\n")

     


available_classes = [["US History", "World History", "US Government"], 
                     ["Physics", "Biology", "Chemistry", "Anatomy"],
                     ["English Composition", "American Literature", "Journalism"], 
                     ["Statistics", "Algebra", "Geometry", "Calculus"], 
                     ["Spanish", "French", "Mandarin"],
                     ["Art", "Ceramics", "Choir", "Band", "Orchestra"]]

# Create a set containing high school students 
all_students = {
    Student("Quinn", "Walker", 10045),
    Student("Riley", "Young", 10046),
    Student("Sophia", "Moore", 10047),
    Student("Theo", "Turner", 10048),
    Student("Ulysses", "Scott", 10049),
    Student("Vivian", "King", 10050),
    Student("Wyatt", "Wright", 10051),
    Student("Ximena", "Martin", 10052),
    Student("Yasmine", "Lopez", 10053),
    Student("Zachary", "Hernandez", 10054),
    Student("Aiden", "Brown", 10055),
    Student("Bella", "Harris", 10056),
    Student("Caleb", "Smith", 10057),
    Student("Daisy", "Davis", 10058),
    Student("Eli", "Lewis", 10059),
    Student("Freya", "Walker", 10060),
    Student("Gabriel", "Young", 10061),
    Student("Hazel", "Moore", 10062),
    Student("Isaiah", "Turner", 10063),
    Student("Jade", "Martin", 10064),
    Student("Kai", "Lopez", 10065),
    Student("Luna", "Perez", 10066),
    Student("Mason", "Wright", 10067),
    Student("Natalie", "Johnson", 10068),
    Student("Oliver", "Lee", 10069),
    Student("Piper", "Lewis", 10070),
    Student("Quincy", "Hall", 10071),
    Student("Rebecca", "Young", 10072),
    Student("Samuel", "Scott", 10073),
    Student("Tessa", "King", 10074),
    Student("Uma", "Wright", 10075),
    Student("Vincent", "Martin", 10076),
    Student("Willow", "Turner", 10077),
    Student("Xander", "Lopez", 10078),
    Student("Yara", "Davis", 10079),
    Student("Zane", "Hernandez", 10080),
    Student("Abigail", "Smith", 10081),
    Student("Benjamin", "Johnson", 10082),
    Student("Catherine", "Brown", 10083),
    Student("David", "Harris", 10084),
    Student("Ella", "Walker", 10085),
    Student("Alice", "Smith", 10001),
    Student("Tom", "Johnson", 10002),
    Student("Charlie", "Brown", 10003),
    Student("David", "Wilson", 10004),
    Student("Emma", "Lee", 10005),
    Student("Frank", "Davis", 10006),
    Student("Grace", "Martinez", 10007),
    Student("Hannah", "Garcia", 10008),
    Student("Isaac", "Rodriguez", 10009),
    Student("Jack", "Hernandez", 10010),
    Student("Katherine", "Lopez", 10011),
    Student("Liam", "Gonzalez", 10012),
    Student("Mia", "Perez", 10013),
    Student("Nathan", "Moore", 10014),
    Student("Olivia", "Taylor", 10015),
    Student("Patrick", "Anderson", 10016),
    Student("Quincy", "Thomas", 10017),
    Student("Rachel", "Jackson", 10018),
    Student("Samuel", "White", 10019),
    Student("Taylor", "Harris", 10020),
    Student("Uma", "Clark", 10021),
    Student("Victor", "Lewis", 10022),
    Student("Wendy", "Hall", 10023),
    Student("Xander", "Walker", 10024),
    Student("Yara", "Young", 10025),
    Student("Zane", "Moore", 10026),
    Student("Ava", "Turner", 10027),
    Student("Ben", "Scott", 10028),
    Student("Cara", "King", 10029),
    Student("Daniel", "Wright", 10030),
    Student("Emily", "Martin", 10031),
    Student("Finn", "Lopez", 10032),
    Student("Gemma", "Perez", 10033),
    Student("Henry", "Hernandez", 10034),
    Student("Ivy", "Brown", 10035),
    Student("Jake", "Harris", 10036),
    Student("Kara", "Smith", 10037),
    Student("Leo", "Davis", 10038),
    Student("Maya", "Williams", 10039),
    Student("Noah", "Johnson", 10040),
    Student("Olivia", "Lee", 10041),
    Student("Nora", "Moore", 10042),
    Student("Oscar", "Lewis", 10043),
    Student("Penelope", "Hall", 10044),
}

populate_classes(all_students, available_classes)

for student in all_students:
    print_classList(student)