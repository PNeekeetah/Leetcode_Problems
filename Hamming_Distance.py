# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:46:54 2021

@author: Nikita
"""
"""
Beats 52 % in terms of runtime and 73 in terms of memory 
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        number = x ^ y
        ones = 0
        while number > 0 :
            ones += number & 1
            number //= 2
        return ones
        