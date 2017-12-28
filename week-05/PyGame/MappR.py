# Mapper

import pygame
from pygame.locals import *
import ImagR
import FilR
import os

# loads tileimages to a list based on a file, the height will determine the tile-size,
# and the width will determine the number of tiles in the list
class Tile_set():

    def __init__(self, filepath, file):

        self.image = ImagR.load_image(filepath, file)
        self.height = self.image.get_height()
        self.width = self.height
        self.size = self.width, self.height
        img_count = self.image.get_width() // self.width
        self.tiles = []

        for i in range(img_count):

            img = pygame.Surface(self.size).convert_alpha()

            img.fill((0, 0, 0, 0))

            img.blit(self.image, (0, 0), (i * self.width, 0, self.width, self.height))

            self.tiles.append(img)

# Map Info
# 0 width
# 1 height
# 2 tileset_file
# 3 theme_file
# 4 game_mode 
# 5 author
# 6 text

# The Map God-Class
class Map():
# create the Map object either Empyt from File or Randomly
    def __init__(self, filepath = '', file = '', mode = ''):
    
        self.data = []
        self.info = []
        self.tilemap = []
        self.colors = []
        self.size = self.width, self.height = 0, 0
        self.filepath = filepath
        self.file = file
        self.mode = mode
        self.tile_file = ''
        self.theme_file = ''
        self.game_mode = 'DM'
        self.author = 'Coon Runner'
        self.text = 'Basic map'
        self.tileset = ''

        if mode == 'F':
            self.file_con = FilR.File_Controller(filepath, file)
            if not self.file_con.test_file():
                print(self.file_con.get_errors())
            else:
                self.data = self.file_con.get_lines()
                self.info = self.data[0].split(';')
                self.size = self.width, self.height = int(self.info[0]), int(self.info[1])
                self.tile_file = self.info[2]
                self.theme_file = self.info[3]
                self.game_mode = self.info[4]
                self.author = self.info[5]
                self.text = self.info[6]
                colorlist = self.data[1].split(';')                
                for i in range(0, 12, 3):
                    self.colors.append((int(colorlist[i]), int(colorlist[i + 1]), int(colorlist[i + 2])))
                for y in range(self.height):
                    tileline = []
                    for x in range(self.width):
                        tileline.append(int(self.data[y + 2][x]))
                    self.tilemap.append(tileline)
                main_dir = os.path.split(os.path.abspath(__file__))[0]                
                grafx_dir = main_dir + "\\GrafX\\"                                                
                self.tileset = Tile_set(grafx_dir, self.tile_file)

    # this method requires a map position and returns a tupple of booleans, 
    # for each is True if the associated tile is a wall 
    def get_tile_type(self, y, x):

        top = False
        bot = False
        left = False
        right = False    
        topleft = False
        topright = False
        botleft = False
        botright = False

        if y > 0:
            if self.tilemap[y - 1][x] == 1:
                top = True
        if y < self.height - 1:
            if self.tilemap[y + 1][x] == 1:
                bot = True
        if x > 0:
            if self.tilemap[y][x - 1] == 1:
                left = True
        if x < self.width - 1:
            if self.tilemap[y][x + 1] == 1:
                right = True    
        if x > 0 and y > 0:
            if self.tilemap[y - 1][x - 1] == 1:
                topleft = True
        if x < self.width - 1 and y > 0:
            if self.tilemap[y - 1][x + 1] == 1:
                topright = True
        if x > 0 and y < self.height - 1:
            if self.tilemap[y + 1][x - 1] == 1:
                botleft = True
        if x < self.width - 1 and y < self.height - 1:
            if self.tilemap[y + 1][x + 1] == 1:
                botright = True
        
        return (top, bot, left, right, topleft, topright, botleft, botright)

    # Creates an image about the map, based on the tilemap and the tileset
        
    def get_map_img(self):
        
        img = pygame.Surface((self.width * self.tileset.width, self.height * self.tileset.height))
        
        tile_border = 2

        tile_third = self.tileset.height // 2

        for y in range(self.height):

            for x in range(self.width):

                tile = pygame.Surface(self.tileset.size).convert_alpha()

                tile.blit(self.tileset.tiles[0], (0,0))

                #tile.fill(self.colors[0])

                if self.tilemap[y][x] == 1:
                    
                    tile_type = self.get_tile_type(y, x)                    
                                
                    color1 = self.colors[3]
                    color2 = self.colors[3]
                    color3 = self.colors[2]
                    color4 = self.colors[3]
                    color5 = self.colors[3]
                    color6 = self.colors[3]
                    color7 = self.colors[1]
                    color8 = self.colors[3]
                    color9 = self.colors[3]
                    color10 = 0
                    color11 = 0                    
                    left_off = 0
                    right_off = 0

                    if tile_type[0]:
                        color1 = self.colors[2]

                    if tile_type[1]:
                        color5 = self.colors[2]
                        color7 = self.colors[2]
                        color9 = self.colors[2]

                    if tile_type[2]:
                        color2 = self.colors[2]
                        color6 = self.colors[1]
                        left_off = tile_border                    

                    if tile_type[3]:
                        color4 = self.colors[2]
                        color8 = self.colors[1]
                        right_off = tile_border

                    if tile_type[6] and tile_type[2] and tile_type[1]:
                        color6 = self.colors[2]
                    
                    if tile_type[7] and tile_type[3] and tile_type[1]:
                        color8 = self.colors[2]

                    if tile_type[2] and tile_type[1] and not tile_type[6]:
                        left_off = 0
                        color6 = self.colors[3]

                    if tile_type[3] and tile_type[1] and not tile_type[7]:
                        right_off = 0
                        color8 = self.colors[3]

                    if tile_type[0] and tile_type[2] and not tile_type[4]:
                        color10 = self.colors[3]
                    
                    if tile_type[0] and tile_type[3] and not tile_type[5]:
                        color11 = self.colors[3]
                    
                    if tile_type[1] and tile_type[2] and not tile_type[0]:
                        color10 = self.colors[3]

                    if tile_type[1] and tile_type[3] and not tile_type[0]:
                        color11 = self.colors[3]

                    # top_left line
                    pygame.draw.rect(tile, color2, (0, 0, tile_border, tile_third + tile_border), 0)

                    # top box
                    pygame.draw.rect(tile, color3, (tile_border, tile_border, self.tileset.width - tile_border * 2, tile_third), 0)

                    # top_right line
                    pygame.draw.rect(tile, color4, (self.tileset.width - tile_border, 0, tile_border, tile_third + tile_border), 0)

                    # bot_left line
                    pygame.draw.rect(tile, color6, (0, tile_third + tile_border, tile_border, self.tileset.height - tile_third - tile_border), 0)

                    # bot_box
                    pygame.draw.rect(tile, color7, (tile_border, tile_third + tile_border * 2, self.tileset.width - tile_border * 2, self.tileset.height - tile_third - tile_border * 3), 0)

                    # bot_right line
                    pygame.draw.rect(tile, color8, (self.tileset.width - tile_border, tile_third + tile_border, tile_border, self.tileset.height - tile_third - tile_border), 0)

                    # topline
                    pygame.draw.rect(tile, color1, (tile_border - left_off, 0, self.tileset.width - tile_border * 2 + left_off + right_off, tile_border), 0)

                    # middle line
                    pygame.draw.rect(tile, color5, (tile_border - left_off, tile_third + tile_border, self.tileset.width - tile_border * 2 + left_off + right_off, tile_border), 0)

                    # bot line
                    pygame.draw.rect(tile, color9, (tile_border - left_off, self.tileset.height - tile_border, self.tileset.width - tile_border * 2 + left_off + right_off, tile_border), 0)

                    # extra miniboxes (topleft and topright)
                    if color10 != 0:
                        pygame.draw.rect(tile, color10, (0, 0, tile_border, tile_border), 0)
                    
                    if color11 != 0:
                        pygame.draw.rect(tile, color11, (self.tileset.width - tile_border, 0, tile_border, tile_border), 0)                

                    #tile.blit(tile_overlay, (0,0))

                img.blit(tile, (x * self.tileset.width, y * self.tileset.height))

        return img

'''    # update all the wall sprites position according to screen x and y offset
    def update_sprite_pos(self, x_off, y_off):
        for sprite in self.sprites:
            sprite.rect.x += x_off
            sprite.rect.y += y_off
            self.test_boxes.append(sprite.rect) '''
        