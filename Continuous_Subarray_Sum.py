# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:43:36 2021

@author: Nikita
"""

"""
First solution i've written was very similar to this; the major 
difference was that it used slices and sum(slice), leading to 
a complexity of O(n^3) likely.

Essentially,
for array_size in range (2,size):
    for start_index in range (0, size - array_size + 1):
        current_sum = sum(nums[start_index : start_index + array_size])


In this version, I've cut down on the complexity by using an array. I 
think this should be O(n^2) and O(n) memory.

It took me about 1 hour to come up with this. 
The solution fails for a very large input because of the time limit;
as far as i'm concerned, this is the absolute limit of good enough 
and maintainability.
"""

class Solution:
    def checkSubarraySum(self, nums: list, k : int ) -> bool:
        size = len(nums)
        subsums = list(nums)
        for array_size in range(2,size + 1):
            for i in range(size - array_size + 1):
                subsums[i] += nums[i+array_size-1]
                if subsums[i] % k == 0:
                    return True 
        return False
