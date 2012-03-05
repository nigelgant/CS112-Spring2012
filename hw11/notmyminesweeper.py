#import

from random import randrange
import pygame
from pygame import draw
from pygame.locals import *


#globals

SCREEN_SIZE = (800, 600)
BACKGROUND = (0, 0, 0)
C_BOMB = (200, 90, 90)
C_BORDER = (230, 80,230)#purple
C_HIDDEN = (100, 100, 100)
C_CLICKED = (0, 0, 0)
C_FLAG = (0, 0, 0)
C_FLAG_INNER = (0, 0, 200)
C_ACTIVE = (34, 55, 98, 80) ## TRY TO FIX THIS
FPS = 30
TEXT_COLORS = [ (255, 0, 0), 
               (175, 75, 0,), 
               (150, 100, 0), 
               (100, 150, 0),
               (50, 200, 0),
               (0, 250, 0),
               (0, 200, 50),
               (0, 150, 100) ]

def loss(world):
    for row in world:
        for cell in row:
            if cell["bomb"]:
                cell["cleared"] = True

def win(world, num_bombs):
    c = 0
    for row in world:
        for cell in row:
            if not cell["cleared"]:
                c += 1
    if c > num_bombs:
        return False
    else:
        return True

def bomb_at(world, x, y):
    width = len(world)
    height = len(world[0])
    
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    else:
        return world[x][y]["bomb"]

def count_touching(world, x, y):
    cell = world[x][y]
    if bomb_at(world, x-1, y-1):
        cell["count"] += 1
    if bomb_at(world, x+1, y+1):
        cell["count"] += 1
    if bomb_at(world, x+1, y-1):
        cell["count"] += 1
    if bomb_at(world, x-1, y+1):
        cell["count"] += 1
    if bomb_at(world, x, y-1):
        cell["count"] += 1
    if bomb_at(world, x+1, y):
        cell["count"] += 1
    if bomb_at(world, x, y+1):
        cell["count"] += 1
    if bomb_at(world, x-1, y):
        cell["count"] += 1


def clear_square(world, x, y):
    world[x][y]["cleared"] = True
    if world[x][y]["bomb"]:
        loss(world)
        return True
    else:
        return False

def deploy_flag(world, x, y):
    world[x][y]["flagged"] = not world[x][y]["flagged"]


def game(tile, width, height, num_bombs):
    #init
    screen = pygame.display.set_mode((width*tile, height*tile))
    buff = screen.convert_alpha()
    FONT = pygame.font.Font(None, 35)
    num_flags = num_bombs
    #flag_image = pygame.surface((tile, tile))
   
    world = []#establishes the grid, a dictionary in each square.
    for x in range(width):
        row = []
        for y in range(height):
            cell = {}
            cell["rect"] = pygame.Rect(x * tile, y * tile, tile, tile)
            cell["cleared"] = False
            cell["bomb"] = False
            cell["count"] = 0
            cell["flagged"] = False
            row.append(cell)
        world.append(row)
    #place bombs
    c = 0
    while c < num_bombs:
        x = randrange(width)
        y = randrange(height)
        if not world[x][y]["bomb"]:
            world[x][y]["bomb"] = True
            c += 1
            
    for x in range(width):
        for y in range(height):
            count_touching(world, x, y)


    ##FLAG
    has_won = False
    game_over = False
    lmb_clicked = False
    rmb_clicked = False
    action_clear_square = False
    action_deploy_flag = False
    #loop
    clock = pygame.time.Clock()
    done = False


    while not done:
        
        #input
        for event in pygame.event.get():#more quitting rules.
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            #mouseright - flags
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:###WIP###
                rmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                rmb_clicked = False
                action_deploy_flag = True
            

            #Mouse/shift (mac's flags)
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and pygame.key.get_mods() & KMOD_SHIFT:#WHAT?
                rmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 1 and pygame.key.get_mods() & KMOD_SHIFT:
                rmb_clicked = False
                action_deploy_flag = True
            
            #mouseleft - clear
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                lmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                lmb_clicked = False
                action_clear_square = True
            

            
        
        #update
        if action_clear_square == True:
            x, y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if not world[x][y]["flagged"]:
                game_over = clear_square(world, x, y)
            action_clear_square = False
        
        has_won = win(world, num_bombs)
        if has_won:
            done = True
            print "Great Job!"

        if action_deploy_flag:
            x, y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if num_flags > 0 and not world[x][y]["flagged"]:
                world[x][y]["flagged"] = True
                num_flags -= 1
            elif world[x][y]["flagged"]:
                world[x][y]["flagged"] = False
                num_flags += 1
            action_deploy_flag = False


        #display
        buff.fill(C_BORDER)
        for x in range(width):
            for y in range (height):
                #get rect
                rect = world[x][y]["rect"]
              #cell color
                
                
                if world[x][y]["cleared"]:
                    bg_color = C_CLICKED
                else:
                    bg_color = C_HIDDEN
                buff.fill(bg_color, rect.inflate(-2, -2))
                
                if world[x][y]["cleared"]:
                    if world[x][y]["bomb"]:
                        pygame.draw.ellipse(buff, C_BOMB, rect.inflate(-tile/2, -tile/2))

                    elif world[x][y]["count"]:
                        count = world[x][y]["count"]
                        text = FONT.render(str(count), True, TEXT_COLORS[count-1], C_CLICKED)
                        loc = text.get_rect()
                        loc.center = rect.center
                        buff.blit(text, loc)
                        

                elif world[x][y]["flagged"]:
                    pygame.draw.ellipse(buff, C_FLAG, rect.inflate(-tile/2, -tile/2))
                    pygame.draw.ellipse(buff, C_FLAG_INNER, rect.inflate(-tile/1.5, -tile/1.5))
                    
                if rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(buff, C_ACTIVE, rect)
        screen.blit(buff, (0,0))

        #refresh
        pygame.display.flip()
        clock.tick(FPS)

#application

def main():
    pygame.init()
    game(50, 10, 10, 10)
    pass



main()
print "bye bye"
