#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""
import math

UserName=raw_input("Enter your name: ")
print "PrissyBot: Hello there", UserName
input=raw_input(UserName+": ")
print "PrissyBot: You mean, '" + input + ", sir!'"

print "PrissyBot: So, " + UserName + ". Do you think your pathetic human brain can handle some simple arithmetic? Y/n"
inp=raw_input(UserName+": [Y/n]")
if inp.lower().startswith("n"):
    print "PrissyBot: I'm glad that you understand the limitations of your puny human cerebrum, however, we are going to do it anyway!"
else: 
    print "PrissyBot: Well aren't we optimistic today!"

n=raw_input("PrissyBot: Ok genius, enter a number: ")
m=raw_input("PrissyBot: Good to see that wasn't too much for you. Now enter another number: ")
n=int(n)
m=float(m)

print "PrissyBot: Now lets perform some simple arithmetic. Try to keep up."

print n,"+",m,"=",n+m
print n,"-",m,"=",n-m
print n,"*",m,"=",n*m
print n,"/",m,"=",n/m

print "PrissyBot: Ok " + UserName + ", take a few minutes to wrap your head around that, and then we will step it up a notch."

a=raw_input("PrissyBot: Ok nerd (ha). This time we are going to do some exponentiation. Go ahead and enter another number when you are ready: ")
b=raw_input("PrissyBot: Horrible choice, now give me another number: ")
print "PrissyBot: Even worse! Anyway, here's the answer."
a=int(a)
b=float(b)

print a,"**",b,"=",a**b
print "PrissyBot: Boom, betcha cant do that in your head."
print "PrissyBot: Alright, I have time for one more math problem, interested? Y/n"

inp=raw_input(UserName+": [Y/n]")
if inp.lower().startswith("n"):
    print "PrissyBot: Oh wait. I just realised that I have no interest in your opinion. Lets do some math!"
else: 
    print "PrissyBot: You are such a NERD! Ok lets do this."    
print "PrissyBot: This time we are going to take two integers, multiply them together and finally take the square root of the whole mess."

x=raw_input("PrissyBot: Ready " + UserName + "? Take a few deep breaths and give me a number between one and infinity: ")
y=raw_input("PrissyBot: Almost done; Just enter one more number: ")
x=int(x)
y=float(y)

print x,"*",y,"=",x*y

print "PrissyBot: Now we take the square root of that and we get:"

print math.sqrt(x*y)
print "PrissyBot: Hey " + UserName + ". Are you still with me?"

inp=raw_input(UserName+": [Y/n]")
if inp.lower().startswith("n"):
    print "PrissyBot: Good, I've been trying to get rid of you for the past 5 minutes now."
else: 
    print "PrissyBot: Really? I was pretty positive that all of that math would scare you away. Well, since your utter existence is an insult to evoluton, why dont you go ahead and jump in a lake."
print "PrissyBot: Have a horrible day! PrissyBot out."
 


 
  




# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.



# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

