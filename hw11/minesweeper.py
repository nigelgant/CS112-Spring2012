#!/usr/bin/wnv python

from random import randrange
import pygame
from pygame.locals import *

#settings
FPS = 30

#Colors
C_BORDER = 0,0,0
C_HIDDEN = 80,80,80
C_ACTIVE = 255,255,255
C_CLEARED = 0,0,255
C_BOMB = 255,0,0
C_FLAG = 0,0,0
C_WIN = 0,255,0

def lose(world,x,y):
    lose = False
    if world[x][y]["cleared"] and world[x][y]["bomb"]:
        lose = True
        for row in world:
            for cell in row:
                if cell["bomb"]:
                    cell["cleared"] = True
    
    return lose

def num_uncleared(world):
    total=0
    for row in world:
        for cell in row:
            if not cell["cleared"]:
                total += 1
    return total
            
def win(num_bombs, not_cleared, lost):
    win = False
    if not lost and num_bombs == not_cleared:
        win = True
    return win
    
    


def clear_square(world,x,y):
    world[x][y]["cleared"] = True

def flag(world,x,y):
    world[x][y]["flagged"] = not world[x][y]["flagged"]

def bomb_at(world,x,y):
    width = len(world)
    height = len(world[0])
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    else:
        return world[x][y]["bomb"]
#game
#give number of bombs touching
def count_touching(world,x,y):
    cell = world[x][y]
    
    if bomb_at(world,x-1,y-1):
        cell["count"] += 1
    if bomb_at(world,x+1,y+1):
        cell["count"] += 1
    if bomb_at(world,x+1,y-1):
        cell["count"] += 1
    if bomb_at(world,x-1,y+1):
        cell["count"] += 1
    if bomb_at(world,x-1,y):
        cell["count"] += 1
    if bomb_at(world,x+1,y):
        cell["count"] += 1
    if bomb_at(world,x,y+1):
        cell["count"] += 1
    if bomb_at(world,x,y-1):
        cell["count"] += 1

def game(tile, width, height, num_bombs):
    #init
    screen = pygame.display.set_mode((width*tile, height*tile))
    font = pygame.font.Font(None, tile/2)
    big_font = pygame.font.Font(None, tile*2)
    num_flags = num_bombs
    
    #store all the game data
    world = []
    for x in range(width):
        row = []
        for y in range(height):
            cell = {}
            cell["cleared"] = False
            cell["bomb"] = False
            cell["rect"] = pygame.Rect(x*tile, y*tile, tile, tile)
            cell["count"] = 0
            cell["flagged"] = False
            row.append(cell)
        world.append(row)
        
        #place bombs
    c= 0
    while c < num_bombs:
        x = randrange(width)
        y = randrange(height)
        if not world[x][y]["bomb"]:
            world[x][y]["bomb"] = True
            c +=1

    # loop through each cell, count touching
    for y in range(height):
        for x in range(width):
            count_touching(world,x,y)
            
        

    #flags
    lmb_clicked = False
    action_clear_square = False
    rmb_clicked = False
    action_flag = False
    lost = False
    won = False

    #loop
    clock = pygame.time.Clock()
    done = False
    while not done:

        #input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            
            #mouse
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                lmb_clicked = True
            elif event.type== MOUSEBUTTONUP and event.button == 1:
                lmb_clicked = False
                action_clear_square = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                rmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                rmb_clicked = False
                action_flag = True
        #update

        if action_clear_square:
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if not lost and not world[x][y]["flagged"]:
                clear_square(world, x, y)
                lost = lose(world, x, y)
            action_clear_square = False
            
        if action_flag:
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if num_flags > 0 and not world[x][y]["flagged"] and not lost:
                flag(world,x,y)
                num_flags -= 1
            elif world[x][y]["flagged"] and not lost:
                flag(world,x,y)
                num_flags += 1
            action_flag = False

        #reveal(lose,world)
               
        #display
        screen.fill(C_BORDER)
        for x in range(width):
            for y in range(height):

                #get rect for cell                
                rect = world[x][y]["rect"]

                if world[x][y]["cleared"]:
                    bg_color = C_CLEARED
                elif lmb_clicked and rect.collidepoint(pygame.mouse.get_pos()):
                    bg_color = C_ACTIVE
                else:
                    bg_color = C_HIDDEN
                
                screen.fill(bg_color, rect.inflate(-2, -2))
                if world[x][y]["cleared"]:
                    if world[x][y]["bomb"]:
                        pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-tile/2, -tile/2))
                    elif world[x][y]["count"]:
                        n = world[x][y]["count"]
                        color = [(255,0,0), (255,0,255), (0,255,0), (0,0,255), (100,0, 255), (255,100,0), (0,100,255), (255,0,100)] 
                        text = font.render(str(n), True, color[n-1])
                        loc = text.get_rect()
                        loc.center = rect.center
                        screen.blit(text,loc)
                elif not world[x][y]["cleared"]and world[x][y]["flagged"]:
                    pygame.draw.rect(screen, C_FLAG, rect.inflate(-tile/2, -tile/2))
                
                if lost:
                    text = big_font.render("You Suck!", True, C_BOMB)
                    loc = text.get_rect()
                    loc.center = screen.get_rect().center
                    screen.blit(text, loc)
                not_cleared = num_uncleared(world)
                won = win(num_bombs, not_cleared, lost)
                if won:
                    text = big_font.render("You Won!", True, C_WIN)
                    loc = text.get_rect()
                    loc.center = screen.get_rect().center
                    screen.blit(text, loc)
        #refresh
        pygame.display.flip()
        clock.tick(FPS)

##aplication
def main():
    pygame.init()
    game(50,10,10,1)

main()
print "bye bye"



