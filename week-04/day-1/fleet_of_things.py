# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

from fleet import Fleet
from thing import Thing

fleet = Fleet()

thing1 = Thing("Get milk")
fleet.add(thing1)
thing1 = Thing("Remove the ostricks")
fleet.add(thing1)
thing1 = Thing("Sand up")
thing1.completed = True
fleet.add(thing1)
thing1 = Thing("Eat rocketlunch")
thing1.completed = True
fleet.add(thing1)

print(fleet)
