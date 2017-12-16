#Lotto

def find_n_max(nlist, n):
    
def lottozo(file_name):    
    try:
        with open(file_name, 'r') as efile:
            lines = efile.readlines()   
    except IOError:
        print('Unable to read file')

    numbers = []

    for line in lines:
        a = line.split(';')
        a[15] = a[15][0:2]
        for i in range(5):
            numbers.append(int(a[11 + i]))

    num_matrix = [0] * 90

    for i in range(len(numbers)):
        num_matrix[numbers[i] -1] += 1
    
    legjobbak = [{'Num' : 0}, {'Occur' : 0}] * 5

    
    for i in range(len(numbers)-1):
    for k in range(len(legjobbak)):
            
    print(num_matrix)
 
lottozo(r'''C:\Users\Miki\greenfox\DonBattery\week-03\day-2\otos.csv''')



