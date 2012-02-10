#!/usr/bin/env python
from hwtools import *
import math

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if n % 2 == 0:
    print "Number is even"
else: 
    print "Number is odd"
    print n,"*",2,"=",n*2   # 2. If n is odd, double it

# 3. If n is evenly divisible by 3, add four
if n % 3 == 0:
    print n,"+",4,"=",n+4

# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if grade <= 100 and grade >= 90:
    print "Your grade is an 'A'"
elif grade <= 89 and grade >= 80:
    print "Your grade is a 'B'"
elif grade <= 79 and grade >=70:
    print "Your grade is a 'C'"
elif grade <= 69 and grade >=60:
    print "Your grade is a 'D'"
else: 
    print "Your grade is an 'F'" 

