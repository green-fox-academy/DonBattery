# Create a method that decrypts encoded-lines.txt

def decrypt(file_name):    
    try:
        with open(file_name, 'r') as efile:
            lines = efile.readlines()   
    except IOError:
        print('Unable to read file')
    decripted = []
    dline = ''
    dchar = ''
    print(lines)
    for line in range(len(lines)):
        for i in range(len(lines[line])):
            dchar = lines[line][i]
            if dchar.isalpha() or dchar in ['[','{','(','"']: 
                dchar = chr(ord(dchar) - 1)
            dline += dchar
        decripted.append(dline)
        dline = ''
    print(decripted)
    try:
        with open('decripted3.txt', 'w') as dfile:
            dfile.writelines(decripted)
    except IOError:
        print('Unable to write to file')

decrypt(r'''C:\Users\Miki\greenfox\DonBattery\week-03\day-2\encoded-lines.txt''')



