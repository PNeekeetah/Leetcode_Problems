# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:39:49 2021

@author: Nikita
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        solutions = []
        def helper(total_numbers, total_sum, last, current_solution = None):
            nonlocal solutions
            if (current_solution is  None):
                current_solution = {}
            if (total_sum == 0) and (total_numbers == 0):
                solutions.append(list(current_solution.keys()))
                return
            if (total_sum < 0) or (total_numbers < 0):
                return
            for i in range(last,10):
                current_solution[i] = 1
                helper(total_numbers-1,total_sum - i, i+1,current_solution)
                current_solution.remove(i)
        helper(k,n,1)
        return solutions
    
"""
Finished function in 14:33
Solution accepted first time
Beats 8.24% in terms of runtime and 84.70% in terms of Memory.
"""