# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:09:48 2021

@author: Nikita
"""
"""
Beats 92 % in terms of runtime
Beats 40 % in terms of memory
Took me about 22 minutes to figure
it out. 
First submission succesful.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        window_start = 0
        window_end = 0
        accumulator = nums[0]
        min_window = len(nums) + 1
        if accumulator >= target:
            return 1
        for i in range(1,len(nums)):
            if accumulator < target:
                accumulator += nums[i]
                window_end = i
            while accumulator >= target:
                window_end = i
                min_window = min(window_end - window_start + 1, min_window)
                accumulator -= nums[window_start]
                window_start += 1
        if min_window == len(nums) + 1:
            return 0
        return min_window
        