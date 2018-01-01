# Drawer

import MappR
import CharactR
import pygame
from pygame.locals import *

# Sprites representing wall tiles
class Tile_Sprite(pygame.sprite.Sprite):

    def __init__(self, img, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        

class Window():

    def __init__(self, width = 0, height = 0, title = '', icon_file = '', mode = ''):
        
        self.test_boxes = []

        self.width = width

        self.height = height

        self.x_off, self.y_off = 0, 0

        self.title = title

        self.icon_file = icon_file

        self.wall_top_sprites = pygame.sprite.Group()
        
        self.wall_sprites = pygame.sprite.Group()

        self.mode = pygame.HWSURFACE

        if mode == 'F':
            self.mode = pygame.FULLSCREEN
        
        if mode == 'N':
            self.mode = pygame.NOFRAME

        if mode == 'W':
            self.mode == pygame.RESIZABLE

        pygame.display.set_caption(self.title)

        self.screen = pygame.display.set_mode((self.width, self.height), self.mode)
        self.background = pygame.Surface((self.width, self.height))
        self.background.convert_alpha()
        self.background.fill((200, 200, 0))

    def init_level(self, level):
        
        self.x_off = (self.width - level.width * level.tileset.width) // 2
        self.y_off = (self.height - level.height * level.tileset.height) // 2
        map_img = level.get_map_img()
        self.get_wall_sprites(level, map_img, self.x_off, self.y_off)
        self.background.blit(map_img, (self.x_off, self.y_off))

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_boxes(self, boxes):
        for box in boxes:
            pygame.draw.rect(self.screen, (255,0,255), box, 1)

    def get_wall_sprites(self, map, map_img, x_off, y_off):
    
        for y in range(map.height):
            for x in range(map.width):
    
                if map.tilemap[y][x] == 1:
    
                    tile_type = map.get_tile_type(y, x)

                    if tile_type[1]:
                        img = pygame.Surface(map.tileset.size)
                        img.blit(map_img, (0, 0), (x * map.tileset.width, y * map.tileset.height, map.tileset.width, map.tileset.height))
                        sprite = Tile_Sprite(img, x * map.tileset.width + x_off, y * map.tileset.height + y_off)                    

                    else:
                        img = pygame.Surface((map.tileset.width, map.tileset.height // 3))
                        img.blit(map_img, (0, 0), (x * map.tileset.width, y * map.tileset.height, map.tileset.width, map.tileset.height // 3))
                        sprite = Tile_Sprite(img, x * map.tileset.width + x_off, y * map.tileset.height + y_off)

                    self.wall_sprites.add(sprite)

    def blit_all(self, unitlist):
        new_list = sorted(unitlist, key=lambda character: character.y_pos)        
        for unit in new_list:
            self.screen.blit(unit.get_image(), (unit.x_pos, unit.y_pos))
        self.wall_sprites.draw(self.screen)
        