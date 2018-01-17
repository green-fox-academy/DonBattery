#!/usr/bin/env python

# Oh, Look all these imports! :S
import os.path # This is needed to determine absolute path to the Graphics, Sound and Level folder
import SoundBlastR # This plays bacground music and sound effects
import DrawR # This controls the window and all the graphics drawn on it
import CharactR # This controls the character movement and animation
import MappR # This controls the map
import CollidR # This is responsible for collosion detection
import pygame # Main library
import sys

from pygame.locals import *
from random import randint

class Coon_game(object):
    def __init__(self):

        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.GAME_TICKS = 16
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self.grafx_dir = os.path.join(self.main_dir, 'GrafX')
        self.soundfx_dir = os.path.join(self.main_dir, 'SoundFX')
        self.lvl_dir = os.path.join(self.main_dir, 'LevelZ')
        self.root = DrawR.Window(640, 480, 'Coon Runner', mode = 'F') # This will be our window (mode W - window, F - fullscreen, N - Noframe, H - hardware accelearated)

        self.controls1 = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
        self.player1 = CharactR.Player(self.grafx_dir, "rocky01.png", self.controls1)
        self.player1.boost = 2
        
        self.controls2 = [K_w, K_s, K_a, K_d]
        self.player2 = CharactR.Player(self.grafx_dir, "rocky02.png", self.controls2)
        self.all_player = [self.player1, self.player2]
        self.player2.boost = 4
        # Set the mouse to invish
        pygame.mouse.set_visible(0)

    def init_map(self, player_list, mode = 'R', file = ''):
        if mode == 'F':
            map = MappR.Map(self.lvl_dir, file, mode = 'F')
            SoundBlastR.play_music(os.path.join(self.soundfx_dir, map.info[3]))
#        for player in player_list:
#            other_player_list = player_list
#            other_player_list.remove(player)
#            player.spawn(map, other_player_list)


        return map

    def move_all(self, unitlist, collider, tick):
        for unit in unitlist:
            if tick < unit.boost:
                unit.move(collider)

    # The Game ;)
    def main(self):
        # Load a map
        # Right now this only can work with a map-file (mode = F), later random-map can be added
        game_map = self.init_map(self.all_player, 'F', 'test_level.lvl') 
        # This generates the graphics of the map (background and wall-sprites)
        self.root.init_level(game_map)
        # This will check the collosions during the game
        collider = CollidR.Collider(game_map, self.root.x_off, self.root.y_off)
        # Game-loop can be quited by seting this to False
        game_on = True

        # Attention travellers! Mainloop ahead!
        self.player1.x_pos = 110
        self.player1.y_pos = 80
        self.player2.x_pos = 80
        self.player2.y_pos = 120
        while game_on:

            self.clock.tick(self.FPS) # Regulate the gamespeed to the given frame per secound

            # Read the event queue and handle the events accordingly (now it is only for quiting)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    game_on = False

            # Read the keystate (which key(s) is(are) pressed on the keyboard right now) and set the character's speed accordingly    
            key_state = pygame.key.get_pressed()

            for unit in self.all_player:
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

            # The main idea behind this sequence is to update the "game-state" n times before updating the display once
            # so we can move gameobjects with different speed
            for tick in range(self.GAME_TICKS):
                # Show the collider-unit where the players are
                collider.update_foot_boxes(self.all_player)
                # Time to move all objects (if possible)
                self.move_all(self.all_player, collider, tick)

            # Draw the background first
            self.root.draw_background()

            # Call the DrawR's intelligent render method to draw the sprites in order to the screen
            self.root.blit_all(self.all_player)

            # . o O TEST ERASE THIS LATER TEST O o .
            #root.test_boxes = collider.foot_boxes
            #root.draw_boxes(root.test_boxes)

            # Display all the rendered graphics onto the screen
            pygame.display.flip()

        pygame.quit()

        print('\nThank you for playing the Coon Runner')
        print('May the Coons be with you :)')

the_game = Coon_game()

if __name__ == '__main__': 
    pygame.init()
    the_game.main()