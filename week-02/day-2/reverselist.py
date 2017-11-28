#Reverse List

aj = [3, 4, 5, 6, 7, 9]
mid = int(len(aj) // 2)

def swap(i1=0, i2=0):
    i3 = aj[i1]
    aj[i1] = aj[i2]
    aj[i2] = i3

print('Before')
print(aj)
print()

if mid > 0:
    for i in range(mid):
        swap(i,int(len(aj)-i-1))


print('After')
print(aj)