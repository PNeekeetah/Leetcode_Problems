# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:15:33 2021

@author: Nikita
"""

"""
Beats 87% in terms of runtime and 18.30% in terms of memory.
First time submission.
"""


class Solution:
    def numSteps(self, s: str) -> int:
        number = int(s,2)
        steps = 0
        while number != 1:
            if number & 1 == 0:
                number >>= 1
            else:
                number += 1
            steps += 1
        return steps
    
