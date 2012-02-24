#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements

def greeter(name):
    name = str(name)
    name = name.lower()
    print "hello,", name

greeter("Enter text")

#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

# def greeter(name):


# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements

def box(w,h):
    if type(w) != int or type(h) != int or w < 1 or h < 1:
        print "Error: Invalid Dimensions"
        return
    
    if w == 1:
        top = "+"
        sides = "|"
    else:
        top = "+" + "-"*(w-2) + "+"
        sides = "|" + " "*(w-2) + "|"
    
    print top
    for i in range (h-2):
        print sides
    if h >=2:
        print top


print box(5,5)
    
    
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

# def box(w,h):



# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()

