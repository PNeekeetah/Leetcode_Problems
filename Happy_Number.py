# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:16:15 2021

@author: Nikita
"""

"""
Took me about 5 minutes to come up with this.

It beats  95% in terms of runtime and 46 %
in terms of memory.

First submission was succesful.

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = {n}
        while n != 1:
            n = sum([int(digit)**2 for digit in str(n)])
            if n not in seen_numbers:
                seen_numbers.add(n)
            else:
                return False
        return True