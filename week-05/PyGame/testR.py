#!/usr/bin/env python

import os.path
import time
import ImagR
import SoundBlastR
import DrawR
import CharactR
import MappR
import pygame
import sys

from pygame.locals import *

clock = pygame.time.Clock()

FPS = 60

main_dir = os.path.split(os.path.abspath(__file__))[0]

grafx_dir = main_dir + "\\GrafX\\"

soundfx_dir = main_dir + "\\SoundFX\\"

print(grafx_dir)

print(soundfx_dir)

root = DrawR.Window(320,240,'', mode = '')

player1 = CharactR.Player(grafx_dir, 'rocky01.png')

def main():

    pygame.init()

    # test sound    
    if pygame.mixer and not pygame.mixer.get_init():
        print ('no sound')
        pygame.mixer = None

    icon = ImagR.load_image(grafx_dir, 'icon.png')
    pygame.display.set_icon(icon)
    pygame.mouse.set_visible(0)

    while True:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()
        
        keystate = pygame.key.get_pressed()
      
        player1.move()

        root.screen.blit(player1.image, (0, 0))

        pygame.display.update()

if __name__ == '__main__': 
    main()