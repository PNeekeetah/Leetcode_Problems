# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:17:36 2021

@author: Nikita
"""

def maxProfit(prices: list()) -> int:
    current_min = prices[0]
    current_min_i = 0
    max_profit = []
    seen = {}
    for i in range(1,len(prices)):
        if prices[i] < current_min:
            current_min = prices[i]
            current_min_i = i
        if max_profit < prices[i] - current_min:
            max_profit = prices[i] - current_min
            seen[current_min_i] = max_profit
    
    buff = []
    for val in seen.values():
        if (len(buff) >= 2):
            if val > buff[0]:
                buff[1] = buff[0]
                buff[0] = val
                
            elif val > buff[1]:
                buff[1] = val
            
        else:
            buff.append(val)
    if (len(buff) == 0):
        return 0
    elif (len(buff) == 1):
        return buff[0]
    else:
        return buff[1]+buff[0]

    
he = maxProfit([1,2,3,4,5,10,1,2,3,4,5,0,6,100,1,2,3,4,100,1,500,1,5000,1,2,2,3,4,5,6,10])

"""
Unsolved as of yet.
"""
