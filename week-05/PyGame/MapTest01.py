#!/usr/bin/env python

from random import randint
import pygame
from pygame.locals import *

# 18, 14 is the max for 640*480

map_size = map_width, map_height = 18, 14

def get_random_map():
    return [[randint(0,1) for x in range(map_width)] for y in range(map_height)]

# DO NOT FORGET : Y comes first !!!!
# map[0][0] = 1

map_color1 = (55,55,0)
map_color2 = (100,100,100)
map_color3 = (155,155,155)
map_color4 = (25,25,25)

def load_image(path, file, mode = ''):
    "loads an image, prepares it for play"
    file = path + file
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if mode == 'A':   
        return surface.convert_alpha()
    else:
        return surface.convert()

def get_tile_type(y, x):

    top = False
    bot = False
    left = False
    right = False    
    topleft = False
    topright = False
    botleft = False
    botright = False

    if y > 0:
        if map[y - 1][x] == 1:
            top = True
    if y < map_height - 1:
        if map[y + 1][x] == 1:
            bot = True
    if x > 0:
        if map[y][x - 1] == 1:
            left = True
    if x < map_width - 1:
        if map[y][x + 1] == 1:
            right = True    
    if x > 0 and y > 0:
        if map[y - 1][x - 1] == 1:
            topleft = True
    if x < map_width - 1 and y > 0:
        if map[y - 1][x + 1] == 1:
            topright = True
    if x > 0 and y < map_height - 1:
        if map[y + 1][x - 1] == 1:
            botleft = True
    if x < map_width - 1 and y < map_height - 1:
        if map[y + 1][x + 1] == 1:
            botright = True
    
    return (top, bot, left, right, topleft, topright, botleft, botright)

def draw_the_map():

    tile_size = tile_width, tile_height = 32, 32 

    tile_border = 2

    random_tile = randint(1,3)

    if random_tile == 1:
        tile_img = load_image('','tile01.png')
    if random_tile == 2:
        tile_img = load_image('','tile02.png')
    if random_tile == 3:
        tile_img = load_image('','tile03.png')

    tile_overlay = tile_img.copy()

    tile_overlay.convert_alpha()

    tile_overlay.set_alpha(125)

    mapoff_x = (screen_w - tile_width * map_width) // 2
    
    mapoff_y =  (screen_h - tile_height * map_height) // 2    

    for y in range(map_height):

        for x in range(map_width):

            tile = pygame.Surface(tile_size).convert_alpha()

            tile.blit(tile_img, (0,0))

            if map[y][x] == 1:
                
                tile_type = get_tile_type(y, x)
                
                tile_third = tile_height // 2
                             
                color1 = map_color4
                color2 = map_color4
                color3 = map_color3
                color4 = map_color4
                color5 = map_color4
                color6 = map_color4
                color7 = map_color2
                color8 = map_color4
                color9 = map_color4
                color10 = 0
                color11 = 0
                
                left_off = 0

                right_off = 0

                if tile_type[0]:
                    color1 = map_color3

                if tile_type[1]:
                    color5 = map_color3
                    color7 = map_color3
                    color9 = map_color3

                if tile_type[2]:
                    color2 = map_color3
                    color6 = map_color2
                    left_off = tile_border                    

                if tile_type[3]:
                    color4 = map_color3
                    color8 = map_color2
                    right_off = tile_border

                if tile_type[6] and tile_type[2] and tile_type[1]:
                    color6 = map_color3
                
                if tile_type[7] and tile_type[3] and tile_type[1]:
                    color8 = map_color3

                if tile_type[2] and tile_type[1] and not tile_type[6]:
                    left_off = 0
                    color6 = map_color4

                if tile_type[3] and tile_type[1] and not tile_type[7]:
                    right_off = 0
                    color8 = map_color4

                if tile_type[0] and tile_type[2] and not tile_type[4]:
                    color10 = map_color4
                
                if tile_type[0] and tile_type[3] and not tile_type[5]:
                    color11 = map_color4
                
                if tile_type[1] and tile_type[2] and not tile_type[0]:
                    color10 = map_color4

                if tile_type[1] and tile_type[3] and not tile_type[0]:
                    color11 = map_color4


                # top_left line
                pygame.draw.rect(tile, color2, (0, 0, tile_border, tile_third + tile_border), 0)

                # top box
                pygame.draw.rect(tile, color3, (tile_border, tile_border, tile_width - tile_border * 2, tile_third), 0)

                # top_right line
                pygame.draw.rect(tile, color4, (tile_width - tile_border, 0, tile_border, tile_third + tile_border), 0)


                # bot_left line
                pygame.draw.rect(tile, color6, (0, tile_third + tile_border, tile_border, tile_height - tile_third - tile_border), 0)

                # bot_box
                pygame.draw.rect(tile, color7, (tile_border, tile_third + tile_border * 2, tile_width - tile_border * 2, tile_height - tile_third - tile_border * 3), 0)

                # bot_right line
                pygame.draw.rect(tile, color8, (tile_width - tile_border, tile_third + tile_border, tile_border, tile_height - tile_third - tile_border), 0)

                # topline
                pygame.draw.rect(tile, color1, (tile_border - left_off, 0, tile_width - tile_border * 2 + left_off + right_off, tile_border), 0)

                # middle line
                pygame.draw.rect(tile, color5, (tile_border - left_off, tile_third + tile_border, tile_width - tile_border * 2 + left_off + right_off, tile_border), 0)

                # bot line
                pygame.draw.rect(tile, color9, (tile_border - left_off, tile_height - tile_border, tile_width - tile_border * 2 + left_off + right_off, tile_border), 0)

                # extra pixels
                if color10 != 0:
                    pygame.draw.rect(tile, color10, (0, 0, tile_border, tile_border), 0)
                
                if color11 != 0:
                    pygame.draw.rect(tile, color11, (tile_width - tile_border, 0, tile_border, tile_border), 0)                

                tile.blit(tile_overlay, (0,0))

            display.blit(tile, (mapoff_x + x * tile_width, mapoff_y + y * tile_height))
    
    pygame.display.update()

if __name__ == "__main__":

    pygame.init()

    pygame.mixer.music.load('doom1.mid')

    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Maptest")

    window_size = screen_w, screen_h = 640, 480

    display = pygame.display.set_mode(window_size, pygame.FULLSCREEN)

    pygame.display.set_icon(load_image('','ico01.png', 'A'))

    FPS = 60

    clock = pygame.time.Clock()

    game_on = True

    map = get_random_map()

    draw_the_map()

    while game_on:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_on = False

            if event.type == KEYUP:
                map = get_random_map()
                draw_the_map()
            
    pygame.quit()

    print('\nBye')