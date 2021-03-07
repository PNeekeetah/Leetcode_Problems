# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:04:23 2021

@author: Nikita
"""

class Solution:
    def fib(self, n: int) -> int:
        
        # Keeps track of values in formal parameters ; Memory is O(n), Runtime O(n)
        # Well, this is also called tail recursion. Python doesn't support tail recursion
        # though, so that's why the memory in this case is O(n).
        def fibRecIter(first : int, second : int, n : int):
            if (n == 0):
                return first
            else:
                return fibRecIter(second, first + second, n - 1)
    
        # Keeps track of values in a dictionary. Memory is O(n), Runtime is O(n)
        seen = {}
        def fibRecMemo(n):
            nonlocal seen
            if seen.get(n):
                return seen[n]
            if (n == 0):
                seen[0] = 0
                return 0
            if (n == 1):
                seen[1] = 1
                return 1
            else:
                value = fibRecMemo(n-1) + fibRecMemo(n-2)
                seen[n] = value
                return value
        
        # Naive implementation. Memory is O(n), Runtime is O(1.6^n) -> Binet's formula
        def fibRec(n):
            if (n == 0):
                return 0
            elif (n == 1):
                return 1
            else:
                return fibRec(n-1) + fibRec(n-2)
            
        
        # Tabulation version. Runtime O(n), memory O(n) -> will be slightly faster than the iterative recursive version    
        def fibIterTab(n):
            fibVals = [0,1]
            if (n == 0):
                return fibVals[0]
            elif(n == 1):
                return fibVals[1]
            for i in range(n-1):
                fibVals.append(fibVals[-2] + fibVals[-1])
            return fibVals[-1]
    
        # O(1) memory and O(n) runtime. Quite fast, calculates fib(10**6) in about 10 seconds
        def fibIter(n):
            if (n == 0):
                return 0
            elif(n == 1):
                return 1
            a = 0
            b = 1
            for i in range(n-1):
                a, b = b, a+b
                
            return b
            
        return fibIter(n)
    
    
        
    
solution = Solution()
print(solution.fib(1000000))
            
            
            
            
"""
6 Minutes and 4 seconds for a succesful submission.

Beats 84% in terms of runtime and 64 % in terms of memory. 

I went ahead and implemented the 4 other flavours i had in mind in about
14 minutes.

The fibIter beats 96% in terms of runtime, but none in terms of memory?
Weird.......

"""