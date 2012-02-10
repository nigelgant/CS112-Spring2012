#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
print "The sum of all numbers is:"
total=0
for num in nums:
    total+=num
print total


# 2. Print every even number in nums
print "All of the even numbers are:"
for num in nums:
   if num % 2 == 0:
       print num


# 3. Does nums only contain even numbers? 


#CODE GOES HERE

some_odd = False
for num in nums:
    if num % 2 != 0:
        some_odd = True
if some_odd == True:
    print "Some odd in the list."

else:
    print "All even."


# 4. Generate a list every odd number less than 100. Hint: use range()
print "Every odd number from 1-100"
odds = []

for i in range(1,100,2):
    odds.append(i)
print odds


# 5. [ADVANCED]  Multiply each element in nums by its index

