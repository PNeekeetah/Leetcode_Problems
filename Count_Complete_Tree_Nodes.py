# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:54:55 2021

@author: Nikita
"""

"""
Beats 5.46 in terms of runtime and 76.23% in terms of memory
It took me 3 minutes 30 to solve it.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        nodes = 0
        def dfs (node : TreeNode):
            nonlocal nodes
            nodes += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        if root:
            dfs(root)
        return nodes