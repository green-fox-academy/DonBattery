import pygame
from pygame.locals import *
import os

# see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Extended image module required")

def load_image(path, file, mode = ''):
    "loads an image, prepares it for play"
    file = os.path.join(path, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if mode == 'A':   
        return surface.convert_alpha()
    else:
        return surface.convert()

def load_images(path = '', *files, mode = ''):
    imgs = []
    for file in files:
        imgs.append(load_image(path, file, mode))
    return imgs