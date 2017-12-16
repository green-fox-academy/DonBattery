# Create a method that decrypts encoded-lines.txt

def decrypt(file_name):    
    try:
        with open(file_name, 'r') as efile:
            lines = efile.readlines()   
    except IOError:
        print('Unable to read file')
    print(lines)
    try:
        with open('decripted3.txt', 'w') as dfile:
            dfile.writelines(decripted)
    except IOError:
        print('Unable to write to file')

decrypt(r'''C:\Users\Miki\greenfox\DonBattery\week-03\day-2\otos.csv''')



