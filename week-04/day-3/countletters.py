#Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
#Create a test for that.

def count_letters(sString):
    letters = {}
    c = ''
    for i in range(len(sString)):
        c = sString[i]
        try:
            if letters[c] != -1:
                letters[c] += 1
        except KeyError:
            letters[c] = 1
    return letters

print(count_letters('ada   dsasda bhgfshgterhrwgfad'))