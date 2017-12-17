
    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

def count_as(file_path):
        rawlist = []
        number_of_a = 0
        try:
            with open(file_path, 'r+') as f_file:
                rawlist = f_file.readlines()
        except FileNotFoundError:
            print('File not found : ', file_path)
            return 0
        except IOError:
            print('Cannot read the file : ', file_path)
            return 0
        except Exception as err:
            print('As I tried to mainpulate : ', file_path)
            print(err)
            return 0
        finally:
            for i in range(len(rawlist)):
                for j in range(len(rawlist[i])):
                    if rawlist[i][j] in ['a', 'A']:
                        number_of_a += 1
            return number_of_a
    
print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
