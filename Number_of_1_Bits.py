# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:37:39 2021

@author: Nikita
"""

"""
Beats 83 % in terms of runtime and 88% in terms of memory
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n > 0:
            ones += n & 1
            n //= 2
        return ones
        