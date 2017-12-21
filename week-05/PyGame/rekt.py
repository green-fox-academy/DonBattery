import pygame
import sys
from random import randint
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 400))

bg = pygame.Surface((400, 400))
bg.fill((44, 111, 222))
screen.blit(bg,(0, 0))
rekt = pygame.Surface((37,37)).convert_alpha()
rekt.fill((123,44,200))
rekt.convert_alpha()


rekt2 = pygame.Surface((54,113)).convert_alpha()
rekt2.set_alpha(120)
rekt2.fill((200,200,0))

coon = pygame.image.load('GrafX\\rocky01.png').convert_alpha()

screen.blit(rekt, (0,0))
screen.blit(rekt2, (10,10))
screen.blit(coon, (13,13))


print('Rekt1 alpha: ', rekt.get_alpha())
print('Rekt2 alpha: ', rekt2.get_alpha())

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
    screen.blit(bg,(0,0))
    screen.blit(coon,(randint(10,200), randint(10,200)))
    print(coon.get_alpha())
    pygame.display.update()


