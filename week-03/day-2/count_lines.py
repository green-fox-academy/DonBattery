# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def linecounter(FFilename):
    try:
        with open(FFilename) as f:
            return len(f.readlines())
    except IOError:
        return 0

print(linecounter('my-file.txt'))

print(linecounter('sajt'))
