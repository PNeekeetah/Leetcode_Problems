# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:41:21 2021

@author: Nikita
"""

"""
First submission successfull
Beats 95% in terms  of runtime and
92% in terms of memory.
"""

class Solution:
    def pivotIndex(self, nums: list) -> int:
        array_sum = sum(nums)
        accumulator = 0
        for i in range (len(nums)):
            if (array_sum - nums[i])/2 == accumulator:
                return i
            accumulator += nums[i]
        return -1
        
solution = Solution()
value = solution.pivotIndex([1,2,3,2,1])