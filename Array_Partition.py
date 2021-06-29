# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:36:58 2021

@author: Nikita
"""

"""
Solved this in about 5 minutes. Runtime 
beats 26% of submissions and memory
usage beats 41.44% of submissions.
"""

class Solution:
    def arrayPairSum(self, nums: list) -> int:
        # sorting puts small numbers together
        nums.sort()
        max_sum = 0 
        for i in range (0,len(nums),2):
            max_sum += min(nums[i],nums[i+1])
        return max_sum