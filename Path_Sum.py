# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:58:18 2021

@author: Nikita
"""

"""
Beats 84% in terms of runtime and 77% in
terms of memory.

Second submission succesful because the
first time I got over-enthusiastic and 
decided to return False when the value 
was smaller than 0 (problem said it's 
possible to have a negative target)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node : "TreeNode", target : int):
    path_exists = False
    
    target -= node.val
    
    if target == 0 and node.left is None and node.right is None:
        return True
    
    if node.left is not None:
        path_exists |= dfs(node.left,target)
    
    if node.right is not None:
        path_exists |= dfs(node.right,target)
    
    return path_exists

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        path_exists = dfs(root,targetSum)
        return path_exists