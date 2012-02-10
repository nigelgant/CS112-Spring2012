#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = 0
while num != 3:
    num=raw_input("Enter a three: ")
    num=int(num)


# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

#CODE GOES HERE
count=0
while count <= 0:
    count=raw_input("Count down from: ")
    count=int(count)

while count>0:
    print count
    count-=3

# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.

# num = int(raw_input("3. Countdown from: "))

