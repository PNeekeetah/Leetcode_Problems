# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:00:07 2021

@author: Nikita
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_recursive(node : "TreeNode", nodes_list : list):
    if node is None:
        return
        
    if node.left is not None:
        postorder_recursive(node.left,nodes_list)
    

    if node.right is not None:
        postorder_recursive(node.right,nodes_list)
        
    nodes_list.append(node.val)

        
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        nodes_list = list()
        postorder_recursive(root, nodes_list)
        return nodes_list