a = []
b = []
size = 9

for i in range(size):
    b = []
    for j in range(size):
        if i == j: 
            b.append('o')
        else:
            b.append('#')
    a.append(b)

for row in a:
    print(" ".join('{0:2}'.format(i or " ") for i in row))

'''   
for i in range(size):
    print(a[i]) '''