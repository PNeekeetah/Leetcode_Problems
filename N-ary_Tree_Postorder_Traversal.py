# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:31:36 2021

@author: Nikita
"""

"""
Beats 98% in terms of runtime
Beats 68% in terms of memory usage

First time submission succesful
Took me 2 minutes to write this
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def postorder_helper(node : "Node",values_list : list) -> list():
    if node is None:
        return []
    
    for child in node.children:
        postorder_helper(child, values_list)
    
    values_list.append(node.val)
    
class Solution:
    def postorder(self, root: 'Node') -> list:
        values_list = list()
        postorder_helper(root, values_list)
        return values_list