# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:33:54 2021

@author: Nikita
"""
"""
Runtime beats 76%
Memory usage beats 82%

First time submission succesful.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs (node : "TreeNode"):
    nodes_list = list()
    queue = list()
    
    if node is None:
        return 0
    queue.append((node,1))
    
    index = 0
    max_level = 0
    while index < len(queue):
        current,level = queue[index]
        if current.left is not None:
            queue.append((current.left,level+1))
        if current.right is not None:
            queue.append((current.right,level+1))
        max_level = max( level, max_level)
        index += 1

    return max_level

class Solution2:
    def maxDepth(self, root: "TreeNode") -> int:
        return bfs(root)

"""
Older attempt
"""

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