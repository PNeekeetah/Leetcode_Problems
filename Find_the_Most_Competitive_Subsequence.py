# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:27:39 2021

@author: Nikita
"""

class Solution:
    def mostCompetitive(self, nums: list(), k: int) -> list():
        last_subsequence_start = len(nums) - k
        stack = []
        for num in nums:
            while (stack and num < stack[-1] and last_subsequence_start > 0):
                stack.pop()
                last_subsequence_start -= 1
            stack.append(num)
        return stack[:k]
    
solution = Solution()
he = solution.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2],3)

"""
After 55 minutes, I throw in the towel. I don't understand the requirements,
nor do I have any idea how to solve this.

Copied this approach entirely from my friend.
"""