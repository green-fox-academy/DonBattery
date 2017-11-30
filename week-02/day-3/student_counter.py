students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def count_candies(Stud):
    candies = 0
    for i in range(len(Stud)):
       candies += (Stud[i]['candies'])
    return candies

def age_candy(Stud):
    age = 0
    for i in range(len(Stud)):
       if Stud[i]['candies'] < 5:
           age += Stud[i]['age']
    return age

# def age_candy():

print("The exact number of the candies owned by students is " + str(count_candies(students)))

print("Sum of the age of people who have lass than 5 candies " + str(age_candy(students)))