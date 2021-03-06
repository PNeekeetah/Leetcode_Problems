# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:40:36 2021

@author: Nikita
"""

class CustomFunction:
    def f(self,x,y):
        return x+y
    def f2(self,x,y):
        return x*y
    
class Solution:

    def findSolution(self,customfunction:CustomFunction,z): # Friend's solution
        final=[]
        x=1
        y=1000
        while (x<=1000 and y>=1):
            prim_rez=customfunction.f(x,y)
            if (prim_rez>z): y=y-1
            elif (prim_rez<z): x=x+1
            else:
                final.append([x,y])
                x=x+1
        return final

    def findSolution(self, customfunction: CustomFunction, z: int) -> list(list()):
        solutions = []
        def rec(x : int,y : int, seen = None):
            if not(seen):
                seen = {}
            if not(seen.get((x,y))):
                seen[(x,y)] = 1
                if (customfunction.f(x,y) == z):
                    solutions.append([x,y])
                    return
                elif (customfunction.f(x,y) > z):
                    return
                rec(x+1,y,seen)
                rec(x,y+1,seen)
        
        rec(1,1)
        return solutions
    
"""
Found this recursive solution in 38 minutes and 41 seconds. 

Beats only 33% in terms of runtime and it beats 7 % in terms of memory.

My friend submitted this problem in about 24 minutes and his solution beats
66 % in terms of runtime and 
"""