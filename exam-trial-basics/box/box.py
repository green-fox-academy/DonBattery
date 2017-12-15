class Cuboid(object):

    def __init__(self, dim_x = 0, dim_y = 0, dim_z = 0):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.dim_z = dim_z

    def get_surface(self):
        return 2 * (self.dim_x * self.dim_y + self.dim_x * self.dim_z + self.dim_y * self.dim_z)

    def get_volume(self):
        return self.dim_x * self.dim_y * self.dim_z
    
    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
