"""
enemy.py
"""

import pygame
from pygame import Surface
from pygame.sprite import Sprite
from random import randrange

class Enemy(Sprite):
    size = width,height = 50,50
    color = 255,0,0
    vx, vy = 6,6

    def __init__(self,loc,bounds):
        Sprite.__init__(self)
        self.image = Surface(self.size)
        self.rect = self.image.get_rect()
        self.bounds = bounds


        self.image.fill(self.color)
        self.rect.bottomleft = loc

        self.vx = randrange(4,8)
        direction = 2 * randrange(2)- 1
        self.vx *= direction

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.rect.x -= 2 * self.vx
            self.vx = -self.vx

        if self.rect.top > self.bounds.bottom:
            self.kill()


class FastEnemy(Enemy):
    color = 255,0,255
    size = width,height = 15,35

    def __init__(self, loc, bounds):
        Enemy.__init__(self,loc,bounds)

        self.vx = 0
        self.vy = 20
