# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was

import os

print("I will draw a square.")
l = input("Enter the side length (1-35): ")
l = int(l)
borderchar = "%"

os.system("clear")

if (l < 1) or (l > 35):
    print("Length out of range!")
elif l == 1:
    print(borderchar)
else:
    for y in range(l):
        if (y == 0) or (y == l-1):
            print(borderchar * l)
        else:
            print((borderchar) + (" " * (l-2)) + (borderchar))
