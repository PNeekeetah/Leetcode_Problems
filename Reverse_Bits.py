# -*- coding: utf-8 -*-
"""
Created on Wed May 26 00:00:57 2021

@author: Nikita
"""

"""
Beats 87 % in terms of runtime and 37 in terms of memory.
First time submission.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        number = 0
        power = 31
        while n > 0 :
            number += n % 2
            number *= 2
            n //= 2
            power -= 1
        if power >= 0:
            number *= 2**power
        else:  
            number //= 2
        return number