# Create a method that decrypts reversed-lines.txt

def decrypt(file_name):    
    try:
        with open(file_name, 'r') as efile:
            lines = efile.readlines()   
    except IOError:
        print('Unable to read file')
    decripted = []
    for line in lines:
        decripted.append(line[::-1])
    try:
        with open('decripted.txt', 'w') as dfile:
            dfile.writelines(decripted)
    except IOError:
        print('Unable to write to file')

decrypt(r'''C:\Users\Miki\greenfox\DonBattery\week-03\day-2\reversed-lines.txt''')


