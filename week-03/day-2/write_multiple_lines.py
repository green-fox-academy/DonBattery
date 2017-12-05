# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.


def writer(_Path, _Word, _Number):
    try:
        with open(_Path,'w') as _File:
            for i in range(_Number):
                _File.write(_Word)
    except IOError:
        return -1

writer(r'''C:\Users\Miki\greenfox\DonBattery\week-03\day-2\my-file.txt''','Sajt\n',99)