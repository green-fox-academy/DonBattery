# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

opened = False

try:
    f = open('my-file.txt', 'r')
    opened = True
except IOError:
    print('Unable to read file: my-file.txt')

if opened:
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
