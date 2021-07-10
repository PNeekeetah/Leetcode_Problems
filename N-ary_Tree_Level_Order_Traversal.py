# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:44:18 2021

@author: Nikita
"""

"""
Beats 38% in terms of runtime
Beats 0% in terms of memory usage

First time submission succesful
Took me about 13 minutes to submit this
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def bfs(root : "Node") -> list:
    if root is None:
        return []
    
    queue = list()
    visited = list()
    current_level = 0
    level_list = list()
    index = 0 
    queue.append((root,0))
    
    queue_length = 1
    while index < queue_length:
        current,level = queue[index]
        queue.extend([(child,level + 1) for child in current.children])
        if level != current_level:
            visited.append(level_list)
            level_list = []
            current_level += 1
            
        level_list.append(current.val)
        index += 1
        queue_length = len(queue)
    else:
        if level_list != []:
            visited.append(level_list)
    return visited
        
class Solution:
    def levelOrder(self, root: 'Node') -> list:
        return bfs(root)
        