# Characters

import pygame
import ImagR

from pygame.locals import *

sprite_size = 34

class Unit():

    def __init__(self, imagepath, imagename):
        image = ImagR.load_image(imagepath, imagename, 'A')
        self.images = []
        for y in range(5):
            for x in range(5):
                surf = pygame.Surface((sprite_size, sprite_size))
                surf.blit(image, (0, 0), (x * sprite_size, y * sprite_size, sprite_size, sprite_size))
                surf.convert_alpha()
                self.images.append(surf)
        for x in range(5):            
            surf = pygame.Surface((sprite_size, sprite_size))
            surf.blit(image, (0, 0), (x * sprite_size, 3 * sprite_size, sprite_size, sprite_size))
            surf = pygame.transform.flip(surf, False, True)
            surf.convert_alpha()
            self.images.append(surf)
        for x in range(5):            
            surf = pygame.Surface((sprite_size, sprite_size))
            surf.blit(image, (0, 0), (x * sprite_size, 2 * sprite_size, sprite_size, sprite_size))
            surf = pygame.transform.flip(surf, False, True)
            surf.convert_alpha()
            self.images.append(surf)
        for x in range(5):            
            surf = pygame.Surface((sprite_size, sprite_size))
            surf.blit(image, (0, 0), (x * sprite_size, sprite_size, sprite_size, sprite_size))
            surf = pygame.transform.flip(surf, False, True)
            surf.convert_alpha()
            self.images.append(surf)

        self.direction = 'S'                
        
        self.anim_count = 0

        self.image = self.get_image()
        
        self.step_counter = 0

        self.x_pos = 0

        self.y_pos = 0

        self.x_spped = 0

        self.y_speed = 0

    def get_image(self):
        if self.direction == 'S':
            off = 0
        elif self.direction == 'SW':
            off = 5
        elif self.direction == 'W':
            off = 10
        elif self.direction == 'NW':
            off = 15
        elif self.direction == 'N':
            off = 20
        elif self.direction == 'NE':
            off = 25
        elif self.direction == 'E':
            off = 30
        elif self.direction == 'SE':
            off = 35
        return self.images[off + self.anim_count]

    def move(self):
        self.x_pos += self.x_spped
        self.y_pos += self.y_speed
        self.step_counter += 1
        if self.step_counter >= 5:
            self.step_counter = 0
            if self.anim_count < 4:
                self.anim_count += 1
            else:
                self.anim_count = 0
        self.image = self.get_image()     

class Character(Unit):
    def __init__(self, imagepath, image):
        super(Character, self).__init__(imagepath, image)

class Player(Character):
    def __init__(self, imagepath, image, controls = ''):
        super(Player, self).__init__(imagepath, image)
        self.controls = controls

class Enemy(Character):
    def __init__(self):
        pass

class Eyeball(Enemy):
    def __init__(self):
        pass