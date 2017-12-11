from domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()

correct = []

correct.append(dominoes.pop(0))

length = len(dominoes)

for i in range(length):
    j = 0
    while correct[i].values[1] != dominoes[j].values[0]:
        j += 1
    correct.append(dominoes.pop(j))

print(correct)