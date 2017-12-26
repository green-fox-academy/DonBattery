# Drawer

import CharactR
import pygame
from pygame.locals import *

class Window():

    def __init__(self, width = 0, height = 0, title = '', icon_file = '', mode = ''):
        
        self.width = width

        self.height = height

        self.x_off, self.y_off = 0, 0

        self.title = title

        self.icon_file = icon_file

        self.mode = pygame.RESIZABLE

        if mode == 'F':
            self.mode = pygame.FULLSCREEN
        
        if mode == 'N':
            self.mode = pygame.NOFRAME

        pygame.display.set_caption(self.title)

        self.screen = pygame.display.set_mode((self.width, self.height), self.mode)
        self.background = pygame.Surface((self.width, self.height))
        self.background.convert_alpha()
        self.background.fill((200, 200, 0))

    def draw_level(self, level):
        self.x_off = (self.width - level.width * level.tileset.width) // 2
        self.y_off = (self.height - level.height * level.tileset.height) // 2
        self.background.blit(level.get_map_img(), (self.x_off, self.y_off))

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_boxes(self, boxes):
        for box in boxes:
            pygame.draw.rect(self.screen, (255,0,255), box, 1)

    def blit_all(self, unitlist):
        for unit in unitlist:
            self.screen.blit(unit.anim, (unit.x_pos, unit.y_pos))
