# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:59:48 2021

@author: Nikita
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        
    def maxDepth(self, root: TreeNode) -> int:
        maxDepth = 0   
        
        def recursiveTraversal(node : TreeNode, depth : int):
            nonlocal maxDepth
            if not node:
                return
            if (depth > maxDepth):
                maxDepth = depth
            if (node.left):
                recursiveTraversal(node.left, depth + 1)
            if (node.right):
                recursiveTraversal(node.right, depth + 1)
        recursiveTraversal(root,1)
        return maxDepth
    
    
"""
I've solved this problem before, but I did it again because I through of a more
elegant solution. 

Took me 4 minutes 33 to code up this solution. Terrible in terms of both runtime
and memory (beats 8% in terms of runtime and 10% in terms of memory).


"""