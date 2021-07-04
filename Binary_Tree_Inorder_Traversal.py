# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:06:37 2021

@author: Nikita
"""

"""
Couldn't figure out the iterative way
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_recursive(node : "TreeNode", nodes_list : list):
    if node is None:
        return
        
    if node.left is not None:
        inorder_recursive(node.left,nodes_list)
    
    nodes_list.append(node.val)

    if node.right is not None:
        inorder_recursive(node.right,nodes_list)
    
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        nodes_list = list()
        inorder_recursive(root,nodes_list)
        return nodes_list