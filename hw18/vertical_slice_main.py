"""
verticle slice main
"""

classes:

Player:
    -Move (user input)
    -jump
    -collide with ground
    -collide with puppy
    -die(resets lvl)

Puppy(goomba):
    -moves until collides or reaches pit
    -collides with player 
    

Floor tiles:
    -nothing.


Specs:
-window size 640,480
-player size 48,32
-puppy size 32,32
