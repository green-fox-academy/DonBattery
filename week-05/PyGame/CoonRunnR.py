#!/usr/bin/env python

# Oh, Look all these imports! :S
import os.path # This is needed to determine absolute path to the Graphics, Sound and Level folder
import SoundBlastR # hmm...
import DrawR # This controls the window and all the graphics drawn on it
import CharactR # This controls the character movement and animation
import MappR # This controls the map
import CollidR # This is responsible for collosion detection
import pygame # Main library
import sys

from pygame.locals import *
from random import randint

clock = pygame.time.Clock()

FPS = 30

GAME_TICKS = 16

main_dir = os.path.split(os.path.abspath(__file__))[0]

grafx_dir = main_dir + "\\GrafX\\"

soundfx_dir = main_dir + "\\SoundFX\\"

lvl_dir = main_dir + "\\LevelZ\\"

# This will be our window (mode W - window, F - fullscreen, N - Noframe, H - hardware accelearated)
root = DrawR.Window(640, 480, 'Coon Runner', mode = 'F')

# Player 1
controls1 = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
player1 = CharactR.Player(grafx_dir, "rocky01.png", controls1)
player1.x_pos, player1.y_pos = 200, 30
player1.direction = 'S'
player1.boost = 7

# Player 2
controls2 = [K_w, K_s, K_a, K_d]
player2 = CharactR.Player(grafx_dir, "rocky02.png", controls2)
player2.x_pos, player2.y_pos = 130, 30
player2.direction = 'NE'
player2.boost = 2

# Player 3
player3 = CharactR.Player(grafx_dir, "rocky03.png", ['e','e','e','e'])
player3.x_pos, player3.y_pos = 130, 60
player3.direction = 'E'

# Player 4
player4 = CharactR.Player(grafx_dir, "rocky04.png", ['e','e','e','e'])
player4.x_pos, player4.y_pos = 130, 90
player4.direction = 'SE'

all_player = []

all_player.append(player1)
all_player.append(player2)
# all_player.append(player3)
# all_player.append(player4)

map1 = MappR.Map(lvl_dir, 'test_level.lvl', mode = 'F')

root.init_level(map1)

collider = CollidR.Collider(map1, root.x_off, root.y_off)

def move_all(unitlist, tick):
    for unit in unitlist:
        if tick < unit.boost:
            unit.move(collider)


def main():

    pygame.init()

    # test sound    
    if pygame.mixer and not pygame.mixer.get_init():
        print ('no sound')
        pygame.mixer = None
    
    # Load and start Map Theme music on loop
    pygame.mixer.music.load(soundfx_dir + map1.info[3])
    pygame.mixer.music.play(-1)

    # Set the mouse to invish
    pygame.mouse.set_visible(0)

    game_on = True

    # Attention travellers! Mainloop ahead!
    while game_on:

        clock.tick(FPS) # Regulate the gamespeed to the given frame per secound

        # Read the event queue and handle the events accordingly
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                game_on = False
            
        key_state = pygame.key.get_pressed()

        for unit in all_player:
            if key_state[unit.controls[0]]:
                unit.y_speed = - 1
            if key_state[unit.controls[1]]:
                unit.y_speed = 1
            if key_state[unit.controls[2]]:
                unit.x_speed = -1
            if key_state[unit.controls[3]]:
                unit.x_speed = 1
            if (key_state[unit.controls[0]] and key_state[unit.controls[1]]) or (not(key_state[unit.controls[0]]) and not(key_state[unit.controls[1]])):
                unit.y_speed = 0
            if (key_state[unit.controls[2]] and key_state[unit.controls[3]]) or (not(key_state[unit.controls[2]]) and not(key_state[unit.controls[3]])):
                unit.x_speed = 0

        for tick in range(GAME_TICKS):
            # Show the collider unit where the players are
            collider.update_foot_boxes(all_player)

            # Time to move all objects (if possible)
            move_all(all_player, tick)

        # Draw the background first
        root.draw_background()

        # Call the DrawR's intelligent render method to draw the sprites in order to the screen
        root.blit_all(all_player)

        # . o O TEST ERASE THIS LATER TEST O o .
        #root.test_boxes = collider.foot_boxes
        #root.draw_boxes(root.test_boxes)

        # Display all the rendered graphics onto the screen
        pygame.display.flip()

    pygame.quit()

    print('\nThank you for playing the Coon Runner')
    print('May the Coons be with you :)')

if __name__ == '__main__': 
    main()
