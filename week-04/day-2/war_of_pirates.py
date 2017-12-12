from pirates import Parrot, Pirate
from random import randint

pirate1 = Pirate('Davy Jhones')

pirate2 = Pirate('Jack Sparrow')

parrot1 = Parrot('Gyurrika', 'red')

for i in range(5):
    print(pirate1.drink_some_rum())
    print(pirate1.hows_it_going_mate())

print(pirate1.hows_it_going_mate())
print(pirate2.grant_familiar(parrot1))

print(pirate1.brawl(pirate2, randint(0, 3)))

print(pirate1.get_info())
print(pirate2.get_info())
