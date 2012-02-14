#!/usr/bin/env python
from random import randint
t1 = 1
user_input = int(raw_input("Enter the number of random intigers: "))
random_int = []
for _ in range(user_input):
    random_int.append(randint(0,20))#appends random ints (1-19) to list
print random_int
while s:
    s = 0
    for var in range(1, user_input):
        if rr[var-1]>rr[var]:
            t1 = rr[var-1]
            t2 = rr[var]
            random_int [var-1] = user_input
            random_int [var] = user_input
            s=1
print random_int
