# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:33:54 2021

@author: Nikita
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list()) -> TreeNode:
        def buildTree(min_index : int, max_index : int):
            nonlocal nums
            mid_index = min_index;
            if min_index >= max_index:
                return None
            for i in range(min_index, max_index):
                if nums[i] > nums[mid_index] : mid_index = i            
            root = TreeNode (nums[mid_index])
            root.left = buildTree(min_index, mid_index)
            root.right = buildTree(mid_index + 1, max_index)
            return root
        
        return buildTree(0, len(nums))
        
solution = Solution()
array = [3,2,1,6,0,5]

node = solution.constructMaximumBinaryTree(array)

"""
25 minutes and 32 seconds.
Beats 25 in terms of memory and 50% in terms of memory. 
"""