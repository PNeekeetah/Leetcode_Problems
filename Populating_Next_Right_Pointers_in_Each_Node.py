# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:18:42 2021

@author: Nikita
"""

"""
Took me 5 minutes to come up with this solution.

I cheated a bit here. I reused my previous bfs implementation
since it suited the task so well.

I am aware I don't need to keep track of the levels since it's
a perfect BT, but since the BFS allowed me to do so I did it 
regardless. 

This can be done directly within the BFS, but that required
small tweaks.

Beats 24% in terms of runtime and 0% in terms of memory.
"""

# Definition for a Node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None, next: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def bfs (node : "TreeNode"):
    queue = list()
    nodes_list = list()
    
    if node is None:
        return []
    
    queue.append((node,0))
    index = 0
    queue_length = 1
    while index < queue_length:
        current,level = queue[index]
        nodes_list.append((current,level))
        if current.left is not None:
            queue.append((current.left,level+1))
        if current.right is not None:
            queue.append((current.right,level+1))
        queue_length = len(queue)
        index += 1
    return nodes_list

class Solution:
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        nodes_list = bfs(root)
        for i in range(len(nodes_list)-1):
            if nodes_list[i][1] == nodes_list[i+1][1]:
                nodes_list[i][0].next = nodes_list[i+1][0]
            else:
                nodes_list[i][0].next = None
        return root
        