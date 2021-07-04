# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 15:18:38 2021

@author: Nikita
"""

"""
Beats 92% in terms of runtime and 73% in terms 
of memory usage.

3rd time submission was succesful because I messed
up a couple of things, namely the key derivation.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_subtree_key(node : "TreeNode", same_subtrees : dict = None) -> str:
    if same_subtrees is None:
        same_subtrees = dict()
    if node is None:
        return ""
    string = ""
    if node.left is not None:
        string += "l"
        string += build_subtree_key(node.left,same_subtrees)
    string += "c" + str(node.val)
    if node.right is not None:
        string += "r"
        string += build_subtree_key(node.right,same_subtrees)
    same_subtrees.setdefault(string,[]).append(node)
    return string


class Solution:
    def findDuplicateSubtrees(self, root: "TreeNode") -> "TreeNode":
        subtrees_dict = dict()
        subtrees_list = list()
        build_subtree_key(root,subtrees_dict)
        for key in subtrees_dict.keys():
            print(key)
            if len(subtrees_dict[key]) > 1:
                subtrees_list.append(subtrees_dict[key][0])
        return subtrees_list
                
        