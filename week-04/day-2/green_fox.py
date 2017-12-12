# Green Fox inheritance exercise

## Person
class Person:
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print("Hi, I'm ", self.name, ", a ", self.age, " years old ", self.gender, ".")
    
    def get_goal(self):
        print("My goal is: Live for the moment!")

## Student
class Student(Person):

    def __init__(self, name, age, gender, previous_organization, skipped_days = 0):
        Person.__init__(self, name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print("Be a junior software developer.")
    
    def introduce(self):
        print("Hi, I'm " + self.name + ", a ", self.age, " year old ", self.gender, " from ", self.previous_organization, " who skipped ", self.skipped_days, " days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

## Mentor
class Mentor(Person):

    def __init__(self, name, age, gender, level):
        Person.__init__(self, name, age, gender)
        if level in ['junior', 'intermediate', 'senior']:
            self.level = level
        else:
            self.level = 'unknown'
    
    def get_gola(self):
        print("Educate brilliant junior software developers.")
    
    def introduce(self):
        print("Hi, I'm ", self.name, ", a ", self.age, " year old ", self.gender, " ", self.level, " mentor.")

## Sponsor
class Sponsor(Person):

    def __init__(self, name, age, gender, company, hired_students = 0):
        Person.__init__(self, name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def introduce(self):
        print("Hi, I'm ", self.name, ", a ", self.age, " year old ", self.gender, " who represents ", self.company, " and hired", self.hired_students, " students so far.")

    def hire(self):
        self.hired_students += 1
    
    def get_goal(self):
        print("Hire brilliant junior software developers.")

## PallidaClass
class PallidaClass:

    def __init__(self, class_name, students, mentors):
        self.class_name = class_name
        self.students = students
        self.mentors = mentors

    def add_student(self, student):
        self.students.append(student)
    
    def add_mentor(self, mentor):
        self.mentors.append(mentor)

    def info(self):
        print("Pallida ", self.class_name, "class has ", len(self.students), " students and ", len(self.mentors), " mentors.")

