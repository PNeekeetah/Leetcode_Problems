# -*- coding: utf-8 -*-
"""
Created on Wed May 26 00:10:55 2021

@author: Nikita
"""

"""
Beats 75% in terms of runtime and 50% in terms of memory

Can write it as a one liner, BUT i feel like this is more natural 
One liner beats 88% in terms of runtime and 95 in terms of memmory
"""
class Solution:
    def missingNumber(self, nums: list) -> int:
        array_sum = sum(nums)
        array_len = len(nums)
        first_n_ints_sum = array_len*(array_len+1)//2 
        return first_n_ints_sum - array_sum
    
    def missingNumberOneLiner(self, nums: list) -> int:
        return len(nums)*(len(nums)+1)//2 - sum(nums)