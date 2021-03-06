# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 01:02:08 2021

@author: Nikita
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # A BST is built according to the following formula:
        # Values that are less than the TreeNode's value are to the left
        # Values that are greater than the TreeNode's values are to the right.
        def recursiveSearch(node : TreeNode):
            nonlocal val
            if not(node):
                return None
            if (node.val == val):
                return node
            if (val < node.val):
                return recursiveSearch(node.left)
            if (val > node.val):
                return recursiveSearch(node.right)
            
        return recursiveSearch(root)
        
"""
It took me 8 minutes and 3 seconds to come up with the recursive solution.
It beats 52% in terms of runtime and none in terms of memory. First submission
was accepted.

Of course, I could have implemented it iteratively, but that was not the point
of these problems.
"""