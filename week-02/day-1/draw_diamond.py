# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

import os

print("I will draw a diamond.")
w = input("Enter the width (1-35): ")
w = int(w)
elem = "#"

# os.system("clear")

if (w < 1) or (w > 35):
    print("Length out of range!")
elif w < 3:
    print(elem)
else:
    if not(bool(w)):
        w -= 1
    mid = int((w-1)/2)
    for y in range(w):
        if y == mid:
            print(elem * w)
        elif y < mid:
            print((" "*(mid-y))+elem*(y+1))
        else:
            print((" "*(y-mid))+elem*(w-y))