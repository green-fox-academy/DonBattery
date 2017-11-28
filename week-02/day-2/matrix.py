a = []
b = []
size = 4

for i in range(size):
    b = []
    for j in range(size):
        if i == j: 
            b.append(' ')
        else:
            b.append('#')
    a.append(b)

for i in range(size):
    print(a[i])