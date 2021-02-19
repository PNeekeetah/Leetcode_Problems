# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:03:38 2021

@author: Nikita
"""
import numpy as np

l = np.array([7,1,5,3,6,4])
l = np.array([7,6,4,2,1])
l = np.array([8,2,4,3,6,1,2,4,6,7,2,2,1,6,1,2,8,0])
l2 = np.convolve(l,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],1)
maximum = 0

"O(n^2) but O(1) space"
for i in range (0, len(l)-1):
    for j in range (i+1, len(l)):
        if (-l[i] + l[j] > maximum):
            maximum = l[j] - l[i]

"O(n) and O(n) memory"
"""        
current_min = prices[0]
minimum = []
for i in range (0, pricesen(prices)):
    if(current_min >  prices[i]):
        current_min = prices[i]
    minimum.append(current_min)
    
current_max = prices[-1]
maximum = [] 
for i in range(pricesen(prices)-1, -1, -1) :
    if(current_max <  prices[i]):
        current_max = prices[i]
    maximum.append(current_max)

maximum.reverse()   
arr = np.array(maximum) - np.array(minimum)
"""

"""
Less memory solution
"""
class Solution:
    def maxProfit(self, prices: list) -> int:
        current_min = prices[0]
        minimum_run = []
        for i in range(len(prices)):
            if (prices[i] < current_min):
                current_min = prices[i]
            minimum_run.append(current_min)
        
        max_profit = 0
        for i in range(len(prices)):
            prospective_profit = prices[i] - minimum_run[i]
            if(max_profit < prospective_profit):
                max_profit = prospective_profit
                
        return max_profit
    
    def maxProfitBetter(self, prices:list) -> int:
        current_min = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if (prices[i] < current_min):
                current_min = prices[i]
            if(prices[i] - current_min > max_profit):
                max_profit = prices[i] - current_min
        return max_profit
        
    
    
"""

f[n] - f[n-1] -> current - prev 

This can clearly be done in O(n^2). But i've solved
a similar problem in the past which required looking at
the first derivative in order to tell which one sequence
of buying and selling was the most profitable. It was done
in one pass, so this has no reason to be done in more than
one pass.

In the previous method, you buy on a negative slope and 
you sell on a positive one.  

It took me 1 hour , 27 minutes and 39 seconds to come up
with a liniar algorithm. It's terrible in terms of both
runtime (27%) and memory, but I was expecting it to work. 

First submission was succesful.

I tried submitting the O(n^2) one as well, turns out
that it exceeds the time limit and thus it is invalid.

1 hour and 53 minutes and 33 seconds : big improvement with 
new code -> beats 42 % in terms of runtimem but still 
terrible in terms of runtime.

Ok, okay, it hit me. I don't actually need to allocate 
any extra memory, I just need to keep track of the current
minimum and then subtract it from the current day and 
attribute it to the maximum sum if the profit is better.

It took me way too long to come up with that : 1 hour 59 and 19 
to come up with that. For some reason though, it's still terrible.
It only beats 48% of submissions. It also beats 22 % of submissions
in terms of memory.

It is O(n) already, I don't think I can do any better.

After searching around, I realised that most submissions do 
exactly the same thing. I thought that Python's min function
is faster than an if statement and I tried coding out
a solution like that, but it turns out it isn't.

"""
