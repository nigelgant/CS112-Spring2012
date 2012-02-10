#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()
# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?
print "Total numbers in list"
print len(nums)

# 2.  Append 3 and 5 to nums
nums.append(3)
nums.append(5)
print nums
print "3 and 5 have been appended to the list."

# 3.  Remove the last element from nums
del nums [len(nums)-1]
print nums
print "The last element has been removed from the list."

# 4.  Set the 3rd element to 7
nums.insert(2,"7")
print nums
print "The third element has been set to '7'"

# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one

# print "5.", nums


# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values

# nums_copy = __
# print "6.", nums, nums_copy

# 7-9. [ADVANCED] Print the following:

# print "7.", nums[__]    # first 3 elements
# print "8.", nums[__]    # last element
# print "9.", nums[__]    # a list of the second element
