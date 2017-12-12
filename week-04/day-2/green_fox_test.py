# green_fox_test

from green_fox import Person, Student, Mentor, Sponsor, PallidaClass
from random import randint

genders = ['male', 'female']
firstnames = ['John', 'Ivan', 'Alice', 'Igor', 'Tolstoj', 'Trockij', 'David', 'Jakab']
surnames = ['Snow', 'Malkovits', 'Braunsweiger', 'Shepard', 'Freeman', 'Ginger']
organizations = ['Salvation Army', 'Navy Seal', 'Red Army', 'Specnaz']
levels = ['junior', 'intermediate', 'senior']
companies = ['IBM', 'Apple', 'Microsoft', 'Blizzard', 'Peoples republic of China']

students = []
mentors = []
sponsors = []
classes = []


for i in range(20):
    students.append(Student((firstnames[randint(0, len(firstnames) - 1)] + " " + surnames[randint(0, len(surnames) - 1)]), randint(18,50), genders[randint(0, len(genders) - 1)], organizations[randint(0, len(organizations) - 1)]))
    sStudent = Student
    students[i].introduce()

for i in range(3):
    mentors.append(Mentor((firstnames[randint(0, len(firstnames) - 1)] + " " + surnames[randint(0, len(surnames) - 1)]), randint(22,50), genders[randint(0, len(genders) - 1)], levels[randint(0, len(levels) - 1)]))
    mentors[i].introduce()

for i in range(3):
    sponsors.append(Sponsor(firstnames[randint(0, len(firstnames) - 1)] + " " + surnames[randint(0, len(surnames) - 1)], randint(30,70), genders[randint(0, len(genders) - 1)], companies[randint(0, len(companies) - 1)]))
    sponsors[i].introduce

classes.append(PallidaClass('B4DC47', students, mentors))

classes[0].info()