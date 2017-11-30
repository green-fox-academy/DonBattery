students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def candy_counter(Stud):
    candyowners = []
    for i in range(len(Stud)):
       if Stud[i]['candies'] > 4:
           candyowners.append(Stud[i]['name'])
    return candyowners

def candy_avarage(Stud):
    sum = 0
    for i in range(len(Stud)):
       sum += Stud[i]['candies']
    return sum / len(Stud)


print("Who has got more candies than 4 candies " + str(candy_counter(students)))

print("How many candies they have on average " + str(candy_avarage(students)))
