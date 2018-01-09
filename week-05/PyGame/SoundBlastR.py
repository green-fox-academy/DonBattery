import pygame
from pygame.locals import *

class dummysound:
    def play(self): 
        pass

def test_sound():
    if pygame.mixer and not pygame.mixer.get_init():
        print ('no sound')
        pygame.mixer = None
        return False
    else:
        return True

def load_sound(file):
    if not pygame.mixer: 
        return dummysound()
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()

def play_music(file, repeat = 0):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(repeat)