#!/usr/bin/env python
import pygame
from pygame.locals import *
from pygame import draw

def red_bike(surf, pos, color=(255,0,0), size=40):
    x,y = pos
    
    width = size/8

    draw.circle(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)
"""
def blue_bike(surf, pos, color=(0,0,255), size=40):
    x,y = pos
    
    width = size/8

    draw.circle(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)
"""
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    screen.fill((0,0,0))
    draw_red_bike(screen, [bike_x, bike_y])
    
    pygame.display.flip()
    clock.tick(30)
    





"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""


