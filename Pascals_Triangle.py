# -*- coding: utf-8 -*-
"""
Created on Wed May 26 22:40:57 2021

@author: Nikita
"""

"""
I don't know a faster or better method than this. You 
have to generate n*(n+1)/2 numbers in total. Well, PERHAPS
you can stop halfway through and mirror the list and append 
the mirrored version, but it still ends up being quadratic.

Solution beats 55% in terms of runtime and 55  in terms of
memory.
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1]]
        if numRows == 1:
            return pascals
        pascals.append([1,1])
        if numRows == 2:
            return pascals
        for row in range (3,numRows+1):
            pascals.append([])
            for col in range(row):
                if col == 0 or col == row-1:
                    pascals[-1].append(1)
                else:
                    value = pascals[-2][col-1] + pascals[-2][col]
                    pascals[-1].append(value)
        return pascals

                
    
sol = Solution()
sol.generate(5)