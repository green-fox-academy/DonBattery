
# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def Checker(NumList = []):
    if (4 in NumList) and (8 in NumList) and (12 in NumList) and (16 in NumList):
        return True
    else:
        return False

print(Checker(list_of_numbers))