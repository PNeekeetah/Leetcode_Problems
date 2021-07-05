# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:21:43 2021

@author: Nikita
"""

"""
Beats 48% in terms of runtime and 0% in terms of memory.
First time submission succesful.

Took me 0 minutes to come up with this since it's the
same solution as for Populating_Next_Right_Pointers_in_Each_Node.py.

There's no coincidence that this solution looks exactly
like the one in Populating_Next_Right_Pointers_in_Each_Node.py.

Since the 2 were next to each other in Leetcode, I assumed the
next problem would ask me to do it for a non perfect BST. The
design for the previous problem took care of this as well.


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