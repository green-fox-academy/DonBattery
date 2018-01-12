#!/usr/bin/env python

import pygame
from pygame.locals import *
import PIL
import os

def get_scale(rect_from, rect_to):
    scale_x = rect_to.w / rect_from.w
    scale_y = rect_to.h / rect_from.h
    if scale_x < scale_y:
        return scale_x
    else:
        return scale_y

class Layout(object):

    def __init__(self, width, height, win):

        self.window = win

        self.size = self.width, self.height = width, height

        self.vertical_fifth = (self.height // 5) * 4

        self.top_frame = pygame.Surface((900, self.vertical_fifth)).convert()
        self.top_frame_rect = self.top_frame.get_rect()

        self.bot_frame = pygame.Surface((900, self.height - self.vertical_fifth)).convert()
        self.bot_frame_rect = self.bot_frame.get_rect()

        self.left_flash = pygame.Surface((self.width // 6, self.vertical_fifth)).convert()
        self.left_flash.set_alpha(0)
        self.left_flash.fill((255, 255, 255))

        self.right_flash = pygame.Surface((self.width // 6, self.vertical_fifth)).convert()
        self.right_flash.set_alpha(0)
        self.right_flash.fill((255, 255, 255))

        self.flash_timer = 0

    def draw_flash(self):
        self.top_frame.blit(self.left_flash, (0, 0))
        self.top_frame.blit(self.right_flash, ((self.width // 6) * 5, 0))

    def draw_middle(self, img):
        self.top_frame.fill((0,0,0))
        img_rect = img.get_rect()
        x_off = 0
        y_off = 0
        scale = get_scale(img_rect, self.top_frame_rect)
        if scale > 1:
            scale = 1
        img = pygame.transform.scale(img, (int(img_rect.w*scale), int(img_rect.h*scale)))
        img_rect = img.get_rect()           
        x_off = (self.top_frame_rect.width - img_rect.width) // 2
        y_off = (self.top_frame_rect.height - img_rect.height) // 2
        self.top_frame.blit(img, (x_off,y_off))

    def update(self):
        if self.flash_timer < 0:
            self.left_flash.set_alpha(abs(self.flash_timer))
            self.flash_timer += 20
        elif self.flash_timer > 0:
            self.right_flash.set_alpha(self.flash_timer)
            self.flash_timer -=20
        if abs(self.flash_timer) < 22:
            self.flash_timer = 0
            self.right_flash.set_alpha(0)
            self.left_flash.set_alpha(0)        

class Window(object):
    
    def __init__(self, width = 0, height = 0, title = '', icon_file = '', mode = ''):

        self.size = self.width, self.height = width, height

        self.title = title

        self.icon_file = icon_file

        self.mode = pygame.HWSURFACE

        if mode == 'F':
            self.mode = pygame.FULLSCREEN
        
        if mode == 'N':
            self.mode = pygame.NOFRAME

        if mode == 'W':
            self.mode == pygame.RESIZABLE
            # Center the window on the screen
            os.environ['SDL_VIDEO_CENTERED'] = '1'
    
        self.screen = pygame.display.set_mode(self.size, self.mode)

        if len(self.icon_file) > 0:
            self.icon = pygame.image.load(self.icon_file)
            pygame.display.set_icon(self.icon)

        pygame.display.set_caption(self.title)

        self.background = pygame.Surface((self.width, self.height))
        self.background.convert()
        self.background.fill((0, 0, 0))


    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

class Gallery_app(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.GAME_TICKS = 20
        self.running = True
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.gallery_dir = os.path.join(self.main_dir, 'gallery')
        self.graphics_dir = os.path.join(self.main_dir, 'graphics')
        self.icon_file = os.path.join(self.graphics_dir, 'icon.ico')

        self.images = []

        self.root = Window(900, 600, '. . o O Image Gallery O o . .', self.icon_file, mode = 'W')
        
        self.layout = Layout(self.root.width, self.root.height, self.root.screen)

        ffile = os.path.join(self.graphics_dir, 'left_flash.png')
        left_flash = self.load_image(ffile)
        self.layout.left_flash.blit(left_flash, (0,0))
        ffile = os.path.join(self.graphics_dir, 'right_flash.png')
        right_flash = self.load_image(ffile)
        self.layout.right_flash.blit(right_flash, (0,0))

        self.loadimages()

        self.max_image = len(self.images)

        self.img_index = 0

        self.set_big()

        self.mouse_delay = 10

    def load_image(self, ffile, mode = ''):
        ffile = os.path.join(self.gallery_dir, ffile)
        try:
            surface = pygame.image.load(ffile)
        except pygame.error:
            raise SystemExit('Could not load image "%s" %s'%(ffile, pygame.get_error()))
        if mode == 'A':   
            return surface.convert_alpha()
        else:
            return surface.convert()

    def loadimages(self):
        filelist = [f for f in os.listdir(self.gallery_dir) if os.path.isfile(os.path.join(self.gallery_dir, f))]
        for ffile in filelist:
            temp_image = {}
            temp_image['file'] = ffile
            temp_image['scale'] = 1
            temp_image['big'] = self.load_image(ffile)
            temp_image['small'] = self.get_small(temp_image['big'])
            self.images.append(temp_image)

    def get_small(self, img):
        img_rect = img.get_rect()
        small_rect = pygame.Rect(0,0,200,118)
        w_diff = 0
        h_diff = 0
        scale = get_scale(img_rect, small_rect)
        return pygame.transform.scale(img, (int(img_rect.w*scale), int(img_rect.h*scale))).convert()

    def draw_smalls(self):
        self.layout.bot_frame.fill((0,0,0))
        for i in range(-1, 2):
            index = self.img_index + i
            if index >= self.max_image:
                index = 0
            if index < 0:
                index = self.max_image - 1
            rect = self.images[index]['small'].get_rect()
            self.layout.bot_frame.blit(self.images[index]['small'], (self.root.width // 2 + i * 200 - 100 + (200 - rect.w) // 2, 2))
        
    def set_big(self):
        self.layout.draw_middle(self.images[self.img_index]['big'])

###############################################################################################
    def render(self):
        self.layout.update()
        self.root.draw_background()
        self.root.screen.blit(self.layout.top_frame, (0, 0))
        self.set_big()
        self.root.screen.blit(self.layout.bot_frame, (0, self.layout.vertical_fifth))
        self.draw_smalls()
        self.layout.draw_flash()
###############################################################################################
    
    def step_left(self):
        self.layout.flash_timer = -255
        self.img_index -=1
        if self.img_index < 0:
            self.img_index = self.max_image - 1
    
    def step_right(self):
        self.layout.flash_timer = 255
        self.img_index += 1
        if self.img_index >= self.max_image:
            self.img_index = 0

    def go(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.running = False
                if event.type == KEYDOWN and event.key == K_LEFT and self.mouse_delay == 0:
                    self.mouse_delay = 20
                    self.step_left()
                if event.type == KEYDOWN and event.key == K_RIGHT and self.mouse_delay == 0:
                    self.mouse_delay = 20
                    self.step_right()
                    
            # Get all the pressed buttons on the mouse
            mouse_buttons = pygame.mouse.get_pressed()
            # Get the mouse's position
            mouse_pos = pygame.mouse.get_pos()
            
            if self.mouse_delay > 0:
                self.mouse_delay -= 1
            else :
                if mouse_buttons[0] and self.layout.top_frame_rect.collidepoint(mouse_pos):
                    self.mouse_delay = 20
                    if mouse_pos[0] < self.root.width // 2:
                        self.step_left()
                    else :
                        self.step_right()                        
                    self.set_big()
      
            self.render()

            pygame.display.flip()

            self.clock.tick(self.FPS)

        pygame.quit()
    
if __name__ == '__main__':
    pygame.init()
    gallery = Gallery_app()
    gallery.go()                         