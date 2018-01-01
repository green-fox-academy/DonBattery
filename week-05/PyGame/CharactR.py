# Characters

import CollidR
import pygame
import ImagR

from pygame.locals import *

sprite_size = 34

# This class represents a character in the game; a player or an enemy
# It has pixel position, speed, and a collection of pictures for each animation frame

class Character():

    def __init__(self, imagepath, imagename):

        image = ImagR.load_image(imagepath, imagename, 'A')

        self.images = []
        self.direction = 'S'              
        self.anim_count = 0
        self.step_counter = 0
        self.x_pos = 0
        self.y_pos = 0
        self.x_speed = 0
        self.y_speed = 0
        self.boost = 2        
        self.anim = pygame.Surface((sprite_size, sprite_size)).convert_alpha()
        self.foot_rect = pygame.Rect(0,0,30,10)

        for y in range(5):
            for x in range(5):
                surf = pygame.Surface((sprite_size, sprite_size)).convert_alpha()         
                surf.fill((0,0,0,0))
                surf.blit(image, (0, 0), (x * sprite_size, y * sprite_size, sprite_size, sprite_size))
                self.images.append(surf)        
        for i in range(3):
            for x in range(5):           
                surf = pygame.Surface((sprite_size, sprite_size)).convert_alpha()
                surf.fill((0,0,0,0))
                surf.blit(image, (0, 0), (x * sprite_size, (3 - i) * sprite_size, sprite_size, sprite_size))
                surf = pygame.transform.flip(surf, True, False)
                self.images.append(surf)
        self.anim = self.get_image()

    # returns the correct self-image based on direction and anim_counter
    def get_image(self):
        
        self.direction = self.get_direction()

        # if direction is 'S'
        off = 0

        if self.direction == 'SW':
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

        self.step_counter += 1
        if self.step_counter > 6 - self.boost:
            self.step_counter = 0
            if self.anim_count < 4:
                self.anim_count += 1
            else:
                self.anim_count = 0

        if self.x_speed == 0 and self.y_speed == 0:
            self.anim_count = 0
    
        return self.images[off + self.anim_count]
    
    # returns the character direction, based on its speed
    def get_direction(self):
        if self.x_speed == 0 and self.y_speed == 1:
            return 'S'
        if self.x_speed == -1 and self.y_speed == 1:
            return 'SW'
        if self.x_speed == -1 and self.y_speed == 0:
            return 'W'
        if self.x_speed == -1 and self.y_speed == -1:
            return 'NW'
        if self.x_speed == 0 and self.y_speed == -1:
            return 'N'
        if self.x_speed == 1 and self.y_speed == -1:
            return'NE'
        if self.x_speed == 1 and self.y_speed == 0:
            return 'E'
        if self.x_speed == 1 and self.y_speed == 1:
            return 'SE'
        if self.x_speed == 0 and self.y_speed == 0:
            return self.direction
    
    def move(self, collider):
        
        if self.x_speed != 0:
            side_test_rect = pygame.Rect(self.x_pos + 7 + self.x_speed, self.y_pos + 23, 20, 9)
            if collider.horizontal_ok(self.foot_rect, side_test_rect):
                self.x_pos += self.x_speed
            
        if self.y_speed != 0:
            topdown_test_rect = pygame.Rect(self.x_pos + 7, self.y_pos + 23 + self.y_speed, 20, 9)
            if collider.vertical_ok(self.foot_rect, topdown_test_rect):
                self.y_pos += self.y_speed

        self.foot_rect = pygame.Rect(self.x_pos+7,self.y_pos + 23, 20, 9)

class Player(Character):
    def __init__(self, imagepath, imagename, controls):
        Character.__init__(self, imagepath, imagename)
        self.controls = controls

class Enemy(Character):
    def __init__(self):
        pass

class Eyeball(Enemy):
    def __init__(self):
        pass
