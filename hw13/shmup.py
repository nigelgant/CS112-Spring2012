 #!/usr/bin/env python

# Space invaders Ikurga, written by Otis Denner-Kenny and Nigel Gant

import sys,os,math
import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group
from random import randrange

C_RED = 255,0,0
C_BLUE = 0,0,255
ENEMY_ONE_WIDTH = 30
ENEMY_ONE_HEIGHT = 20
BULLET_WIDTH = 5
BULLET_HEIGHT = 15
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 30

"""
def load_image(name, colorkey=None):
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey,RLEACCEL
    return image,image.get_rect()
"""

class Spawner(object): #spawns enemy1 in formation
    def __init__(self, width, height, bounds):
        self.width = width 
        self.height = height
        self.bounds = bounds
        self.enemy_group = pygame.sprite.Group()
        self.vx = 2
        self.vy = 0
        self.x = 0
        self.y = 0
        self.color = C_RED
        
    def spawn(self):
        for enemy in range(48):
            if self.x / self.width < 12:
                self.x += self.width
            elif self.x / self.width == 12:
                self.y += self.height
                self.x = self.width
                if self.color == C_RED:
                    self.color = C_BLUE
                else:
                    self.color = C_RED
            #self.y += self.height
            self.enemy_group.add(Enemy1(self.x, self.y, self.vx, self.vy, self.bounds, self.color))
            if self.color == C_RED:
                self.color = C_BLUE
            else:
                self.color = C_RED
                   
class Mother(Sprite):
    width = 20
    height = 20
    def __init__(self,x,y,vx,vy,bounds,color):
        Sprite.__init__(self)
        #color_r = C_RED
        #color_b = C_BLUE
        self.color = color
        self.vx = vx
        self.vy = vy
        self.bounds = bounds

        self.rect = Rect(x,y,self.width,self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()

    def draw_image(self):
        self.image.fill(self.color)

class Bullet(Mother):
    width = BULLET_WIDTH
    height = BULLET_HEIGHT
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right or\
                self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.kill()        

class Enemy1(Mother):
    width = ENEMY_ONE_WIDTH
    height = ENEMY_ONE_HEIGHT

    def __init__(self, x, y, vx, vy, bounds, color):
        Mother.__init__(self, x, y, vx, vy, bounds, color)
        self.x_dist = 0
        self.y_dist = 0

    def update(self):

        vert_count = 6

        if self.y_dist < vert_count:
            self.rect.x += self.vx
            self.x_dist += abs(self.vx)
            
        if self.y_dist >= vert_count:
            self.rect.y += 8

        elif self.x_dist >= self.width*2:
            self.rect.y += self.height
            self.y_dist += 1
            self.vx = -self.vx
            self.x_dist = 0
            
        if self.rect.bottom > self.bounds.bottom:
            self.kill()

            #print enemies.enemy_group 

class Player(Mother):
    def update(self):
        self.x += self.vx


## Game


# init
"""
done = False
pygame.init()
screen = pygame.display.set_mode((600,1000))
clock = pygame.time.Clock()
enemies = pygame.sprite.Group()
enemies = Spawner(40,40,screen.get_rect())
enemies.spawn()


bullet1 = Enemy1(300, 300, 2, 2, screen.get_rect(), C_RED)
bullet2 = Bullet(12, 12, 2, 0, screen.get_rect(), C_RED)
bullets.add(bullet1)

while not done:
    #input 

    #update
    enemies.enemy_group.update()
        
    # draw
    screen.fill((255,255,255))    
    enemies.enemy_group.draw(screen)

    #print bullet1.alive(), bullet2.alive(), len(bullets), list(bullets)

    pygame.display.flip()
    clock.tick(30)
"""
done = False
class Game(object):
    title = "Poops for Outer Space!"
    done = False
    screen_size = 600, 800 
    fps = 30
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.title)
        self.screen.fill((255,255,255))
        self.color = C_BLUE
        self.x, self.y = 300, (800-PLAYER_HEIGHT)
        self.vx, self.vy = 0,0
        self.bounds = self.screen.get_rect()
    def handle_event(self, event):
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pass
                elif event.key == K_LEFT:
                    self.vx = -2
                elif event.key == K_RIGHT:
                    self.vx = 2
                elif event.key == K_x:
                    if self.color == C_BLUE:
                        self.color = C_RED
                    else:    
                        self.color = C_BLUE
        print self.x, self.y, self.vx, self.vy, self.color
    def update(self):
        print self.x
       # pygame.screen.flip()
    def loop(self):
       
        while not done:
            self.handle_event(self)
            self.update
            
#    Player(self.x,self.y,self.vx,self.vy,self.bounds,self.color)
Game().loop()
