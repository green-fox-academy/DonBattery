import os

l = input("Side length (1-35): ")
l = int(l)
borderchar = "@"

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




''' a = "O"

x = "." * 10

a = a + x + "O"

print(a) '''
