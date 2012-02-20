#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

n = len(nums)
for x in range(n):
    pos = x
    for i in range(x+1, n):
        if nums[i] < nums[pos]:
            pos = i
            
    nums[x], nums[pos] = nums[pos], nums[x]

print "After sort:"
print nums
