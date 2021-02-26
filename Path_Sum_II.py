# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:46:44 2021

@author: Nikita
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.solutions = []
        return 
    
    def helper(self,node : TreeNode, targetSum : int, path = None) -> list:
            if (path == None):
                path = []
            if not(node):
                return
            if (targetSum - node.val == 0) and not(node.left) and not(node.right):
                path.append(node.val)
                self.solutions.append(path)
                return
            path.append(node.val)    
            if (node.left):
                pathcopy_left = list(path)
                self.helper(node.left, targetSum - node.val, pathcopy_left)
            if (node.right):
                pathcopy_right = list(path)
                self.helper(node.right, targetSum - node.val, pathcopy_right)
        
            return 
    
    def pathSum(self, root: TreeNode, targetSum: int) -> list(list()):
        
        self.helper(root, targetSum)
        return self.solutions
    
"""
Came up with this solution in about 45 minutes, not exactly great
in terms of runtime (53% better than the others) or memory (5% better than the rest).

Still a lot left to optimize, especially memory wise.
"""