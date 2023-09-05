import random

class Student:
    def __init__(self, first_name, last_name, student_number):

        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.classes = set()

 
    def __eq__(self, other):
        """
        Checks whether two student Objects are one in the same using their attributes. 
        """
        # First ensure that both variables are Student objects.
        if isinstance(other, Student):
            return (
                # Check that their attributes match
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.student_number == other.student_number
            )
        return False
    

    def __hash__(self):
        """
        Computes a hash value based on the attributes of the
        Student object.
        """
        return hash((self.first_name, self.last_name, self.student_number))


def print_classList(student):
    """
    Displays all six classes assigned to a student.
    """
    print(f"\n\nClass Schedule for {student.first_name} {student.last_name}:\n")
    
    for i, class_name in enumerate(student.classes, start=1):
        print(f"Class {i}: {class_name}")


def populate_classes(students, classes):
    """
    Gives every student one class from all six categories available:
    social studies, science, english, math, foreign languages, and electives.
    The order of categories and classes selected will be random per student.
    """
    for student in students:
        # Randomizing the classes may seem unnecessary considering that
        # elements added to a set don't always maintain their original order. 
        # But, enough may not move to make this step useful.
        random.shuffle(classes)

        for category in classes:
            class_assigned = random.choice(category)
            student.classes.add(class_assigned)


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
    Student("Emily", "Martin", 10031),
    Student("Finn", "Lopez", 10032),
    Student("Gemma", "Perez", 10033),
    Student("Henry", "Hernandez", 10034),
    Student("Ivy", "Brown", 10035),
    Student("Jake", "Harris", 10036),
    Student("Vincent", "Martin", 10076),
    Student("Willow", "Turner", 10077),
    Student("Xander", "Lopez", 10078),
    Student("Maya", "Williams", 10039),
    Student("Noah", "Johnson", 10040),
    Student("Olivia", "Lee", 10041),
    Student("Patrick", "Anderson", 10016),
    Student("Quincy", "Thomas", 10017),
    Student("Rachel", "Jackson", 10018),
    Student("Samuel", "White", 10019),
    Student("Taylor", "Harris", 10020),
    Student("Nora", "Moore", 10042),
    Student("Oscar", "Lewis", 10043),
    Student("Penelope", "Hall", 10044),
    Student("Isaac", "Rodriguez", 10009),
    Student("Jack", "Hernandez", 10010),
    Student("Katherine", "Lopez", 10011),
    Student("Liam", "Gonzalez", 10012),
    Student("Mia", "Perez", 10013),
    Student("Nathan", "Moore", 10014),
    Student("Olivia", "Taylor", 10015),
    Student("Uma", "Clark", 10021),
    Student("Victor", "Lewis", 10022),
    Student("Wendy", "Hall", 10023),
    Student("Xander", "Walker", 10024),
    Student("Yara", "Young", 10025),
    Student("Zane", "Moore", 10026),
    Student("Abigail", "Smith", 10081),
    Student("Benjamin", "Johnson", 10082),
    Student("Catherine", "Brown", 10083),
    Student("David", "Harris", 10084),
    Student("Ella", "Walker", 10085),
    Student("Alice", "Smith", 10001),
    Student("Tom", "Johnson", 10002),
    Student("Ava", "Turner", 10027),
    Student("Ben", "Scott", 10028),
    Student("Cara", "King", 10029),
    Student("Daniel", "Wright", 10030),
    Student("Kara", "Smith", 10037),
    Student("Yara", "Davis", 10079),
    Student("Zane", "Hernandez", 10080),
    Student("Charlie", "Brown", 10003),
    Student("David", "Wilson", 10004),
    Student("Emma", "Lee", 10005),
    Student("Frank", "Davis", 10006),
    Student("Grace", "Martinez", 10007),
    Student("Hannah", "Garcia", 10008),
    Student("Leo", "Davis", 10038)
}


# Every student will have one class randomly chosen per category.
available_classes = [["US History", "World History", "US Government"], 
                     ["Physics", "Biology", "Chemistry", "Anatomy"],
                     ["English Composition", "American Literature", "Journalism"], 
                     ["Statistics", "Algebra", "Geometry", "Calculus"], 
                     ["Spanish", "French", "Mandarin"],
                     ["Art", "Ceramics", "Choir", "Band", "Orchestra"]]


populate_classes(all_students, available_classes)


###################
#    Problem 1    #
###################
def is_student(first_name, last_name, student_number, all_students):
    """
    Checks to see if a Student object is in all_students set. HINT: Remember
    that each Student object was fed into the hashing function to determine 
    its hash table location, so an object is going to be needed again to check 
    for membership.
    """

    # The hash value of student_to_find is found using the __hash__ method.
    student_to_find = Student(first_name, last_name, student_number)
    if student_to_find in all_students:
        print(f"{first_name} {last_name} is a student.\n")
    else:
        print(f"{first_name} {last_name} is not a student.\n")


###################
#    Problem 2    #
###################
def add_student(first_name, last_name, student_number, all_students):
    print("student")


###################
#    Problem 3    #
###################
def remove_student(first_name, last_name, student_number, all_students):
    """
    There are two approaches that can be used in this function. Sets have
    'remove' method, which removes an element that's been found in the set.
    However, an error will be raised if the element turns out not to be
    a member of the set.

    Sets also have a 'discard' method, which either removes a found element,
    or does nothing if the element isn't actually in the set.
    """
    print("student")



print("\n\n=========== PROBLEM 1 TESTS ===========\n")
is_student("Aiden", "Brown", 10055, all_students)         # Aiden Brown is a student.
is_student("Katherine", "Turner", 10051, all_students)    # Katherine Turner is not a student.
is_student("Finn", "Anderson", 10078, all_students)       # Finn Anderson is not a student.
is_student("Yasmine", "Lopez", 10053, all_students)       # Yasmine Lopez is a student.

print("\n\n=========== PROBLEM 2 TESTS ===========\n")
print("\n\n=========== PROBLEM 3 TESTS ===========\n")
print("\n\n=========== PROBLEM 4 TESTS ===========\n")

