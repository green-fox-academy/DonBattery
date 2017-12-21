import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time


    
imgPath = "GrafX/"

sprite_size = 34

timer = pygame.time.Clock()

class Unit():
    def __init__(self, screen, image_name, anim_time, start_x = 0, start_y =0):
        self.timer = pygame.time.Clock()
        self.time_now = time.time()
        self.anim_time = anim_time
        self.next_time = self.time_now + self.anim_time
        self.image_name = image_name
        self.images = pygame.image.load(imgPath + image_name).convert_alpha()
        self.pos =[start_x, start_y]
        self.screen = screen
        self.animcount = 0
        self.direction = 'N'

    def render(self):
        if self.direction == 'N':
            anim_off = 20
            anim_flip = False
        if self.direction == 'NE':
            anim_off = 15
            anim_flip = True
        if self.direction == 'E':
            anim_off = 10
            anim_flip = True
        if self.direction == 'SE':
            anim_off = 5
            anim_flip = True
        if self.direction == 'S':
            anim_off = 0
            anim_flip = False
        if self.direction == 'SW':
            anim_off = 5
            anim_flip = False
        if self.direction == 'W':
            anim_off = 10
            anim_flip = False
        if self.direction == 'NW':
            anim_off = 15
            anim_flip = False
        anim_x = (self.animcount + anim_off) % 5
        anim_y = (self.animcount + anim_off) // 5
        self.screen.blit(self.images, (self.pos[0], self.pos[1]), (anim_x * sprite_size, anim_y * sprite_size, sprite_size, sprite_size))
    
    def go_to(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def do_anim(self, till = 0):
        self.time_now = time.time()
        if  self.time_now > self.next_time:
            self.next_time = time.time() + self.anim_time
            if self.animcount < till:
                self.animcount += 1
            else:
                self.animcount = 0 

pygame.init()

pygame.mixer.music.load('doom1.mid')

pygame.mixer.music.play()

pygame.display.set_caption("RPGame")

screen_w, screen_h = 320, 200

screen = pygame.display.set_mode((screen_w, screen_h)) # , pygame.FULLSCREEN
#print(screen.get_alpha())
player1 = Unit(screen, 'rocky04.png', 0.15)

FPS = 160

#The background
back = pygame.Surface((screen_w, screen_h)) 
background = back.convert() # Convert to have the same pixel format as the display Surface.
background.fill((200, 200, 20))

player1_vx = 0
player1_vy = 0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 24)

# Some test TXT
score1 = font.render("WHERE IS YOUR GOD NOW ???", True,(255,255,255))

# Turn off mouse
pygame.mouse.set_pos(screen_w,screen_h)
pygame.mouse.set_visible(False)

# Test rekt
rekt = pygame.Surface((37,37))
rekt.fill((123,44,200))
rekt.convert_alpha()

# main loop
while True:
    timer.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                player1_vy = -1
            if event.key == K_DOWN:
                player1_vy = 1
            if event.key == K_LEFT:
                player1_vx = -1
            if event.key == K_RIGHT:
                player1_vx = 1
            if event.key == K_ESCAPE:
                exit()
        
        if event.type == KEYUP:
            if event.key == K_UP:
                if player1_vy == -1: 
                    player1_vy = 0
            if event.key == K_DOWN:
                if player1_vy == 1: 
                    player1_vy = 0
            if event.key == K_LEFT:
                if player1_vx == -1: 
                    player1_vx = 0
            if event.key == K_RIGHT:
                if player1_vx == 1: 
                    player1_vx = 0

    if -1 <  player1.pos[0] + player1_vx < screen_w - sprite_size - 1:
        player1.pos[0] += player1_vx

    if -1 < player1.pos[1] + player1_vy < screen_h - sprite_size - 1:   
        player1.pos[1] += player1_vy

    screen.blit(background,(0,0))
    screen.blit(rekt, (100, 100))
    print('Back :', screen.get_alpha())
    print('Screen :', screen.get_alpha())
    print('Player :', player1.images.get_alpha())
    if player1_vx == 0 and player1_vy == -1:
        player1.direction = 'N'
    if player1_vx == 1 and player1_vy == -1:
        player1.direction = 'NE'
    if player1_vx == 1 and player1_vy == 0:
        player1.direction = 'E'
    if player1_vx == 1 and player1_vy == 1:
        player1.direction = 'SE'
    if player1_vx == 0 and player1_vy == 1:
        player1.direction = 'S'
    if player1_vx == -1 and player1_vy == 1:
        player1.direction = 'SW'
    if player1_vx == -1 and player1_vy == 0:
        player1.direction = 'W'
    if player1_vx == -1 and player1_vy == -1:
        player1.direction = 'NW'

    player1.do_anim(4)

    player1.render()

    screen.blit(score1,(0,0)) 
    print(player1.images.get_alpha())
    print()
    pygame.display.update()

