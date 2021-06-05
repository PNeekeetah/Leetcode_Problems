# -*- coding: utf-8 -*-
"""
Created on Sun May 30 09:26:35 2021

@author: Nikita
"""
"""
Submission not accepted due to the time limit being exceeded. 

It can probably be done in one pass, but hey ho. Finished in
24:48.
"""

class Solution:
    def find132pattern(self, nums: list) -> bool:
        for k in range (len(nums)):
            for j in range (k):
                for i in range(j):
                    bool1 = nums[i] < nums[k]
                    bool2 = nums[k] < nums[j]
                    if bool1 and bool2:
                        return True
        return False
    
    def find132patternQuadraticSolution(self, nums: list) -> bool:
        sol_set = set()
        for k in range (len (nums) ):
            for j in range (k):
                bool2 = nums[k] < nums[j]
                if bool2 :
                    sol_set.add((j,nums[k]))
                    
        for sol in sol_set:
            for i in range (sol[0]):
                bool1 = nums[i] < sol[1]
                if bool1: 
                    return True
                
        return False
        
                    
array = [1,2,3,4,5,6,7,1,54,5,2,57,1]
                    
solution = Solution()
sol =  solution.find132pattern1(array)
      