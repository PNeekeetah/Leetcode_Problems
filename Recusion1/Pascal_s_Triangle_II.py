# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 01:20:50 2021

@author: Nikita
"""

class Solution:
    def getRow(self, rowIndex: int) -> list():
        # the recursive formula is as follows:
        """
        if (y == 0):
            return 1
        elif (x == y)
            return 1
        else:
            return pascal(x-1,y-1) + pascal(x-1,y)
        """
        # to save a bit of time, we could also use a dictionary to store the intermediate values rather than make recursive calls
        def recursivePascal(x : int, y : int):
            nonlocal seen
            if (seen.get((x,y))):
                return seen[(x,y)]
            else:
                if (y == 0):
                    seen[(x,y)] = 1
                    return 1
                elif (x == y):
                    seen[(x,y)] = 1
                    return 1
                else:
                    value = recursivePascal(x-1,y-1) + recursivePascal(x-1,y)
                    seen[(x,y)] = value
                    return value
        seen = {}        
        rowValues = list()
        for i in range(rowIndex+1):
            rowValues.append(recursivePascal(rowIndex,i))
        
        return rowValues
    
        def getRow(self, rowIndex: int) -> list:
            rowIndex = rowIndex + 1
            if (rowIndex == 1):
                return [1]
            rowValues = list()
            value = 1
            rowValues.append(value)
            for i in range (1,rowIndex-1):
                value = value*(rowIndex-i)/i
                rowValues.append(int(value))
            rowValues.append(1)
            return rowValues
        

        
    
"""
Submission in 15 minutes and 31 seconds.

I thought about using memoization to keep track of the recursive calls to
cut short the waiting time at the expense of memory. 

My solution beats 96.95 % of the solutions, although I have low confidence
in this value because I submitted it again earlier and I got around 61% 
faster in runtime (I resubmitted because I was unsure what the last value was).
It beats nothing in terms of memory ( very likely due to memoization)

If I were to do it iteratively, i'd simply do:
value = 1
for i in range (1,rowIndex+1):
    value *= ((rowIndex-i)/i)  # This is a mistake/ (rowIndex-i) / i can be float.
    rowValues.append(value)...
    
I went ahead and implemented the iterative way as well.
The first succesful submission beats 66% of submissions in terms of runtime
and 94% in terms of memory. Who knew it could be done iteratively? (snide 
comment, i knew it could be done iteratively).

I can probably make it even better by doing it for only half the values and then
mirroring it.


"""