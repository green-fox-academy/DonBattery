# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chicks = input("How many chickens you have? ")
pigs = input("How many pigs you  have?")
legs = int(chicks)*2+int(pigs)*4
print("Your animals has "+str(legs)+" legs in total.")