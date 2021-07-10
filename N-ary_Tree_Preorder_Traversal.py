# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:28:30 2021

@author: Nikita
"""

"""
Beats 8 % in terms of runtime 
Beats 89% in terms of memory utilization

First time submission succesful
Took me 5 minutes to code this
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def preorder_helper(node : "Node",values_list : list) -> list():
    if node is None:
        return []
    values_list.append(node.val)
    for child in node.children:
        preorder_helper(child, values_list)

class Solution:
    def preorder(self, root: 'Node') -> list:
        values_list = list()    
        preorder_helper(root, values_list)
        return values_list