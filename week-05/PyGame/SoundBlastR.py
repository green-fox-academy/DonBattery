import pygame
from pygame.locals import *

class dummysound:
    def play(self): 
        pass

def load_sound(file):
    if not pygame.mixer: 
        return dummysound()
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()