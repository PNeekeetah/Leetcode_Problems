# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 13:43:57 2021

@author: Nikita
"""

"""
Beats 96% in terms of runtime and none in 
terms of memory.

I used the iterative method to get this
result.

I managed to get both right the first 
time I submitted.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_dfs_recursive(node : "TreeNode", nodes_list : list):
    if node is None:
        return
    
    nodes_list.append(node.val)
    
    if node.left is not None:
        preorder_dfs_recursive(node.left,nodes_list)
    
    if node.right is not None:
        preorder_dfs_recursive(node.right,nodes_list)
    

def prerorder_iterative(node : "TreeNode"):
    nodes_list = list()
    stack = list()

    if node is None:
        return []
    
    stack.append(node)
    while stack:
        current = stack.pop()
        nodes_list.append(current.val)
        
        if current.right is not None:
            stack.append(current.right)
        
        if current.left is not None:
            stack.append(current.left)
            
    return nodes_list
        
        
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodes_list = list()
        nodes_list = prerorder_iterative(root)
        #preorder_dfs_recursive(root,nodes_list)
        return nodes_list