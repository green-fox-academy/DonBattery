#!/usr/bin/env python

import os.path
import time
import ImagR
import SoundBlastR
import DrawR
import CharactR
import MappR
import CollidR
import pygame
import sys

from pygame.locals import *
from random import randint

clock = pygame.time.Clock()

FPS = 60

main_dir = os.path.split(os.path.abspath(__file__))[0]

grafx_dir = main_dir + "\\GrafX\\"

soundfx_dir = main_dir + "\\SoundFX\\"

lvl_dir = main_dir + "\\LevelZ\\"

root = DrawR.Window(640, 480, '', mode = 'F')

# Player 1
controls1 = [K_DOWN, K_LEFT, K_UP, K_RIGHT]
player1 = CharactR.Player(grafx_dir, "rocky01.png", controls1)
player1.x_pos, player1.y_pos = 200, 30
player1.direction = 'S'

# Player 2
controls2 = [K_s, K_a, K_w, K_d]
player2 = CharactR.Player(grafx_dir, "rocky02.png", controls2)
player2.x_pos, player2.y_pos = 30, 30
player2.direction = 'NE'

# Player 3
player3 = CharactR.Player(grafx_dir, "rocky03.png", ['e','e','e','e'])
player3.x_pos, player3.y_pos = 130, 30
player3.direction = 'E'

# Player 4
player4 = CharactR.Player(grafx_dir, "rocky04.png", ['e','e','e','e'])
player4.x_pos, player4.y_pos = 30, 130
player4.direction = 'SE'

all_unit = []

all_unit.append(player1)
all_unit.append(player2)
all_unit.append(player3)
all_unit.append(player4)

map1 = MappR.Map(lvl_dir, 'test_level.lvl', 'F')

root.draw_level(map1)

wall_coll = CollidR.Wall_collider(map1, root.x_off, root.y_off)

def move_all(unitlist):
    for unit in unitlist:
        unit.move(wall_coll)

def main():

    pygame.init()

    # test sound    
    if pygame.mixer and not pygame.mixer.get_init():
        print ('no sound')
        pygame.mixer = None

    pygame.mouse.set_visible(0)

    root.draw_level(map1)

    root.draw_background()

    game_on = True

    while game_on:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_on = False
            
            if event.type == KEYDOWN:
                for unit in all_unit:
                    if isinstance(unit, CharactR.Player):                            
                        if event.key == unit.controls[0]:
                            unit.y_speed = 1
                        if event.key == unit.controls[1]:
                            unit.x_speed = -1
                        if event.key == unit.controls[2]:
                            unit.y_speed = -1
                        if event.key == unit.controls[3]:
                            unit.x_speed = 1

            if event.type == KEYUP:
                for unit in all_unit:
                    if isinstance(unit, CharactR.Player):                            
                        if event.key == unit.controls[0]:
                            if unit.y_speed == 1:
                                unit.y_speed = 0
                        if event.key == unit.controls[1]:
                            if unit.x_speed == -1:
                                unit.x_speed = 0
                        if event.key == unit.controls[2]:
                            if unit.y_speed == -1:
                                unit.y_speed = 0
                        if event.key == unit.controls[3]:
                            if unit.x_speed == 1:
                                unit.x_speed = 0      

        move_all(all_unit)

        #for unit in all_unit:
        #    wall_coll.unit_collider(unit)

        root.draw_background()

        root.blit_all(all_unit)

        pygame.display.update()

    pygame.quit()

    print('\nThank you for playing the Coon Runner')
    print('May the Coons be with you :)')

if __name__ == '__main__': 
    main()
