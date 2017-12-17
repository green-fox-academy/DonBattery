default = 50

class Animal(object):
    hunger = 0
    thirst = 0
    name = ""

    def __init__(self, name):
        self.name = name
        self.hunger = default
        self.thirst = default
    
    def eat(self):
        if self.hunger > 0:
            self.hunger -= 1

    def drink(self):
        if self.thirst > 0:
            self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1