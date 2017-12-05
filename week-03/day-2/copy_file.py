# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copier(Path1, Path2):
    try:
        with open(Path1, 'r') as file_from:
            file_content = file_from.readlines()
            with open(Path2, 'w') as file_to:
                file_to.writelines(file_content)
    except IOError:
        return False
    return True

copier(r'''C:\Users\Miki\greenfox\DonBattery\week-03\day-2\my-file.txt''',r'''C:\Users\Miki\greenfox\DonBattery\week-03\day-2\my-file2.txt''')