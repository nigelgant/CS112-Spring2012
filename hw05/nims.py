#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""
import math

number_stones = raw_input("Enter the starting number of stones: ")
number_stones = int(number_stones)

player = 1

print "Max number of stones per turn: 5"

while number_stones > 0:
    # get move
    print number_stones, "stones left. Player ", player, "[1-5]: ",
    inp = raw_input()
    inp = int(inp)
    # is valid move
    if inp > 0 and inp <= 5 and inp <= number_stones:
        # take away stones
        number_stones -= inp
        if player == 2:
            player = 1
        else:
            player = 2
    else:
        print "Invalid move"

print "Player", player, "wins!"
        






