# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

a1 = input("Please enter the value of A1 ")
a2 = input("Please enter the value of A2 ")
a3 = input("Please enter the value of A3 ")
a4 = input("Please enter the value of A4 ")
a5 = input("Please enter the value of A5 ")

a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
a4 = int(a4)
a5 = int(a5)

sum = a1 + a2 + a3 + a4 + a5

avarage = sum / 5

print("The Sum of As is "+str(sum)+" And their Avarage is "+str(avarage))
