# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:37:16 2021

@author: Nikita
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0,1]
        for i in range (n):
            stairs.append(stairs[-1] + stairs[-2])
        return stairs[-1]





global ways
ways = 0

def stairs(n : int):
    global ways
    if (n == 0):
        ways += 1
    if (n < 0):
        return
    stairs(n-1)
    stairs(n-2)
    
total_ways = []
for i in range (20):
    ways = 0
    stairs(i)
    total_ways.append(ways)

modn = 15
fibo = [0,1,1]
for i in range (100):
    fibo.append((fibo[-1] + fibo[-2])%modn)

solution = Solution()
print(solution.climbStairs(30))
    

"""
Alright, so. I've written a small script called 
"stairs" that makes recursive calls. It's good enough
to be used to study the pattern.

Alright, alright, i'm dumb. I stared at the numbers for 2 good
seconds. I was wondering HMMMMMMMMMMM, THIS SEEMS TO LOOK A LOT 
LIKE THE FIBONACCI SEQUENCE. BETTER WRITE THE FIBONACCI SEQUENCE
AND CHECK WHETHER IT'S THE SAME. Spoilers, it's the same. If you
look at the structure of both "stairs" and the iterative 
Fibonacci sequence, you quickly realise why. 

Final submission : 13 minutes and 38 seconds. Accepted first time
It beats 99% of submissions in terms of runtime and it beats 91% 
in terms of memory. 
Submission code is in the "Solution" class.

I bet memory consumption can be improved by popping the first element,
but that probably worsens the runtime.

Could probably be done even quicker with a generator.

"""

