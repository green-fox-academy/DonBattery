#!/usr/bin/env python

import pygame
from pygame.locals import *
import PIL
import os

class Button(pygame.sprite.Sprite):

    def __init__(self, img1, img2, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img1 = img1
        self.img2 = img2       
        self.rect.x = x
        self.rect.y = y
        self.click_timer = 0
        self.image = self.img1
        self.rect = self.image.get_rect() # get rect lol XD
    
    def got_clicked(self):
        self.image = self.img2
        self.click_timer = 15
    
    def update(self): 
        if self.click_timer > 0:
            self.click_timer -= 1
            if self.click_timer == 0:
                self.image = self.img1

class Window(object):
    
    def __init__(self, width = 0, height = 0, title = '', icon_file = '', mode = ''):
        
        self.test_boxes = []

        self.width = width

        self.height = height

        self.title = title

        self.icon_file = icon_file

        
        self.x_off, self.y_off = 0, 0

        self.mode = pygame.HWSURFACE

        if mode == 'F':
            self.mode = pygame.FULLSCREEN
        
        if mode == 'N':
            self.mode = pygame.NOFRAME

        if mode == 'W':
            self.mode == pygame.RESIZABLE
    
        self.screen = pygame.display.set_mode((self.width, self.height), self.mode)

        if len(self.icon_file) > 0:
            self.icon = pygame.image.load(self.icon_file)
            pygame.display.set_icon(self.icon)
        pygame.display.set_caption(self.title)
        self.background = pygame.Surface((self.width, self.height))
        self.background.convert_alpha()
        self.background.fill((0, 0, 0))

        if mode == 'W':
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        
    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

class Gallery_app(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.GAME_TICKS = 1
        self.running = True
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.gallery_dir = os.path.join(self.main_dir, 'gallery')
        self.graphics_dir = os.path.join(self.main_dir, 'graphics')
        self.icon_file = os.path.join(self.graphics_dir, 'icon.ico')

        self.root = Window(900, 600, 'Image Gallery', self.icon_file, mode = 'W')
    
    def go(self):
        while self.running:

            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.running = False
            
            self.root.draw_background()

            pygame.display.flip()

        pygame.quit()
    
gallery = Gallery_app()

if __name__ == '__main__':
    pygame.init()
    gallery.go()