# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:54:27 2021

@author: Nikita
"""
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bit_mask = 1
        shifts = max(len(bin(a))-2,len(bin(b))-2,len(bin(c))-2)
        flips = 0
        
        for i in range(shifts):
            if (((a | b) & bit_mask) == (bit_mask & c)):
                pass
            else:
                if bit_mask & c > 0 :
                    flips += (not (bit_mask & a > 0))
                elif (bit_mask & c == 0):
                    flips += (bit_mask & a > 0) + (bit_mask & b > 0)
            bit_mask = bit_mask << 1
        return flips



hello = minFlips(3,8,5)    



"""
Finished problem in 33:42

Initially, I said "continue" rather than "pass" and I failed. Nonetheless, it
beats 80% in terms of runtime and 54.74% in terms of memory.       

 
"""