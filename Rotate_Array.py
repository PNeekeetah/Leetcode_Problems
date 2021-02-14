# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:17:15 2020

@author: Nikita

First idea :
Sounded like a nice idea but it doesn't work
for i in range(len(nums)):
    index = (i+k)%len(nums)
    nums[i] = nums[i] + nums[index]
    nums[index] = nums[i] - nums[index]
    nums[i] = nums[i] - nums[index]
    print(nums)
"""

nums = [1,2,3,4,5,6,7]
k = 3

# Correct solution, but runtime is bad for some reason
for i in range((-k)%len(nums)):
    nums.insert(0,nums.pop(-1))
    
nums = [1,2,3,4,5,6,7]
print(nums[len(nums)-k:])
print(nums[:len(nums)-k])

# Best solution in terms of time : one liner 
nums = nums[len(nums)-k:]+nums[:len(nums)-k]

"""
    Takeaway :
        slicing in python is way faster than popping and appending in a for loop
"""