# Drawer

import pygame
from pygame.locals import *

class Window():

    def __init__(self, width = 0, height = 0, title = '', icon_file = '', mode = ''):
        
        self.width = width

        self.height = height

        self.title = title

        self.icon_file = icon_file

        self.mode = pygame.RESIZABLE

        if mode == 'F':
            self.mode = pygame.FULLSCREEN
        
        if mode == 'N':
            self.mode = pygame.NOFRAME

        pygame.display.set_caption(self.title)

        self.screen = pygame.display.set_mode((self.width, self.height), self.mode)
