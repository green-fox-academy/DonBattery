from anim import Animal


animalses = []

allat = Animal("Tiger")

animalses.append(allat)

print(animalses[0].name, animalses[0].hunger)

animalses[0].play()

print(animalses[0].name, animalses[0].hunger)