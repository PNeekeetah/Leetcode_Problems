# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:46:54 2021

@author: Nikita
"""
"""
Powers of three:  beats 5.32 in terms of runtime and 48% in terms of memory.
It took me 13:34 minutes to come up with this. I got it right the 3rd time I
submitted it.

The hacky method does it without loops. The runtime jumps at 37% and memory 
usage is slightly better on average, at the cost of readability.

Well, I absolutely LOVE the O(1) runtime O(1) memory solution. It uses the
fact that there's a limitation to how big an integer can be. This beats 74% 
in terms of runtime and 99% in terms of memory, BUT THIS IS NOT MY SOLUTION
THOUGH.

"""
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        powers_of_three = dict()
        iterator = 0
        power = 3**iterator
        upper_bound = 2**31
        while power < upper_bound:
            powers_of_three[power] = 1
            iterator += 1
            power = 3**iterator
        return n in powers_of_three
    


    def special_floor(self,n):
        tentative_floor = math.floor(n)
        if tentative_floor + 0.999 < n:
            return tentative_floor + 1
        else:
            return tentative_floor
        
    def isPowerOfThree1(self, n: int) -> bool: # hacky method
        if n <= 0:
            return False
        else:
            return 3**self.special_floor(math.log(n,3)) == n
        
    def isPowerOfThreeMostEfficient(self, n: int) -> bool:
        if n <= 0 :
            return False
        return 3**19 % n == 0
