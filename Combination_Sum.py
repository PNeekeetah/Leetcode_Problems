# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:21:49 2021

@author: Nikita
"""

class Solution:
    def combinationSum(self, candidates: list(), target: int) -> list(list()):
        solution = list()
        def combo(curr_target,curr_sol,position):
            nonlocal solution, candidates
            if (curr_target == 0):
                solution.append(curr_sol)
                return
            if (curr_target < 0):
                return
            if (curr_target > 0):
                for elem in range (position, len(candidates)):
                    combo(curr_target - candidates[elem],curr_sol + [candidates[elem]], elem)
        combo(target,[],0)
        return solution



can = [5,10,8,4,3,12,9]
tar = 27
solution = Solution()
hey = solution.combinationSum(can,tar)
print(hey)


# Current : 1 hour and 12 minutes + 1 hour 27 and 26 seconds = 2 hours 39 and 26.
# I declare this problem failed because I choose to give up. 
# I am generating all possible permutations of all possible solutions, but I have no idea how to select one 
# of the permutations. 
"""
I've thrown in the towel after 2 hours, 39 minutes and 26 seconds. 
I was stuck trying to find a way of uniquely identifying each permutation
of the solution. 
I noticed that my friend did essentially the exact same thing I did, only that
his solution also kept track of the current position and passed it as a formal
parameter. That apparently stops the generation of the same permutation twice.

This threw me off for a bit because this was actually a Backtracking problem,
not a Dynamic programming one. It was very similar to Combination Sum 4 in 
the beginning (which is a Dynamic Programming problem).

Well, nonetheless. Failed after 2 hours and 39 minutes. Kudos to my friend's
solution.
"""