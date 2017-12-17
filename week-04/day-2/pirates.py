class Being:

    def __init__(self, name):
        self.name = name
        self.isalive = True    

class Parrot(Being):
   
    def __init__(self, name, color):
        Being.__init__(self, name)
        self.color = color
        

class Pirate(Being):    

    def __init__(self, name):
        Being.__init__(self, name)
        self.familiar = []
        self.rum_counter = 0
        self.sane = True

    def get_info(self):
        if self.isalive:
            if self.sane:
                msg = "and is on hes feet"
            else:
                msg = "and is lying on the floor"
            return self.name + " the pirate has drunk " + str(self.rum_counter) + " rums " + msg
        else:
            return self.name + " the pirate is dead"

    def grant_familiar(self, parrot):
        self.familiar.append(parrot)
        return self.name + " aquiered " + self.familiar[-1].name + " the " + self.familiar[-1].color + " parrot"

    def drink_some_rum(self):
        if self.isalive:
            if self.sane:
                self.rum_counter += 1
                return "Cheers matey!"
            else:
                return "zzzzz"
        else:
            return "is dead"

    def hows_it_going_mate(self):
        if self.isalive:
            if self.sane and self.rum_counter <= 4:
                return "Pour me anudder!"
            elif self.sane and self.rum_counter > 4:
                self.sane = False
                self.rum_counter = 0
                return self.name + " has fallen on the floor, passed out."
            else:
                self.sane = True
                return "Harrrrr!!!"            
        else:
            return "is dead"
            
    def die(self):
        self.isalive = False

    def brawl(self, Pirate, chance):
        if self.isalive:
            if self.sane and Pirate.isalive and Pirate.sane:
                if chance == 0:
                    if len(self.familiar) > 0:
                        parrot = self.familiar.pop()
                        return parrot.name + " has died for you"
                    else:
                        self.die()
                        return "lost"
                elif chance == 1:
                    if len(Pirate.familiar) > 0:
                        parrot = Pirate.familiar.pop()
                        return parrot.name + " has died for " + Pirate.name
                    else:
                        Pirate.die()
                        return "won"
                else:
                    self.sane = False
                    Pirate.sane = False
                    return "draw"
            else:
                return "nobrawl"
        else:
            return "is dead"

class Captain(Pirate):

    def __init__(self, name):
        Pirate.__init__(self, name)

class PirateShip():

    def __init__(self, name, cannons = 0, rumstock = 0, Captain = None,  crew = None):        
        self.name = name
        self.cannons = cannons
        self.rumstock = rumstock
        self.captain = captain
        self.crew = crew
    
    def add_captain(self, Captain):

    def add_crewmember(self, Pirate):
    
    def fightship(self, PirateShip):

    

class Armada():

    def __init__(self, name, ships = None):
        self.name = name
        self.ships = ships