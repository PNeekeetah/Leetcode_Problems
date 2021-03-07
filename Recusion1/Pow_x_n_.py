# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 17:20:13 2021

@author: Nikita
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # This is that problem that was done russian multiplication i.e.:
        # You multiply the number with itself regardless/ Write n in binary form / if %2  == 1, multiply with
        # said power if 2. If not, skip.
        
        def russianMultiplication(n : int, acc : float = 1.0):
            nonlocal no
            if (n == 0):
                return acc
            if (n%2):
                acc = acc*no
                no = no*no
                return russianMultiplication(n // 2, acc)
            else:
                no = no*no
                return russianMultiplication(n // 2, acc)
        no = 0
        if (n < 0):
            no = 1/x
        if (n > 0):
            no = x
            
        return russianMultiplication(abs(n))

"""
Submitted this problem in 16 minutes and 37 seconds. First submission was succesful.

My submission beats 63% in terms of runtime.

Naturally, I could have done it iteratively, but again, this isn't the
point of these exercises.
"""        