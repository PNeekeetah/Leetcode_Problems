# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:17:27 2021

@author: Nikita
"""

"""
Beats 94% in terms of runtime and 
12% in terms of memory usage.

My 4th attempt was succesful. The reason
is that I messed up the dfs traversal.

I swear debugging that took longer than the
Count_Vowels_Permutation.py problem.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found_p = False
        found_q = False
        ancestor_dict = dict()
        ancestor_dict[root] = None
        
        def dfs (node : "TreeNode", ancestor_dict : dict) -> None:
            nonlocal found_p, found_q, p, q
            if found_p and found_q:
                return
            if node == p:
                found_p = True
            if node == q:
                found_q = True
            if node.left is not None:
                ancestor_dict[node.left] = node
                dfs(node.left, ancestor_dict)
            if node.right is not None:
                ancestor_dict[node.right] = node
                dfs(node.right, ancestor_dict)
                
        dfs(root,ancestor_dict)
        current_p = p
        current_q = q
        common_ancestor = None
        
        path_p = set()
        while current_p is not None:
            path_p.add(current_p)
            current_p = ancestor_dict.get(current_p)
        
        while current_q is not None:
            if current_q in path_p:
                common_ancestor = current_q
                break
                
            current_q = ancestor_dict.get(current_q)
            
        return common_ancestor