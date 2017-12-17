''' Create a Pirate class. While you can add other fields and methods, you must have these methods:-

drink_some_rum() - intoxicates the Pirate some
hows_it_going_mate() - when called, the Pirate replies, if drink_some_run was called:-
0 to 4 times, "Pour me anudder!"
else, "Arghh, I'ma Pirate. How d'ya d'ink its goin?", the pirate passes out and sleeps it off.
If you manage to get this far, then you can try to do the following.

die() - this kills off the pirate, in which case, drinkSomeRum, etc. just result in he's dead.
brawl(x) - where pirate fights another pirate (if that other pirate is alive) and there's a 1/3 chance, 1 dies, the other dies or they both pass out.
And... if you get that far...

Add a parrot.
 '''

class Parrot():
   
    def __init__(self, name, color):
        self.isalive = True    
        self.name = name
        self.color = color
        

class Pirate():
    

    def __init__(self, name):
        self.name = name
        self.familiar = []
        self.rum_counter = 0
        self.sane = True
        self.isalive = True

    def grant_familiar(self, parrot):
        self.familiar.append(parrot)
        return (self.name, " aquiered ", self.familiar[-1].name, " the ", self.familiar[-1].color, " parrot")

    def drink_some_rum(self):
        if self.isalive:
            self.rum_counter += 1
            return "Cheers matey!"
        else:
            return "is dead"

    def hows_it_going_mateself(self):
        if self.isalive:
            if self.sane and self.rum_counter <= 4:
                return "Pour me anudder!"
            elif self.sane and self.rum_counter > 4:
                self.sane = False
                self.rum_counter = 0
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
                        return (parrot.name, " has died for you")
                    else:
                        self.isalive = False
                        return "lost"
                elif chance == 1:
                    if len(Pirate.familiar) > 0:
                        parrot = Pirate.familiar.pop()
                        return (parrot.name, " has died for ", Pirate.name)
                    else:
                        Pirate.isalive = False
                        return "won"
                else:
                    self.sane = False
                    Pirate.sane = False
                    return "draw"
            else:
                return "nobrawl"
        else:
            return "is dead"

