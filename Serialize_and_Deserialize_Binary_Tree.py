# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 13:20:54 2021

@author: Nikita
"""

"""
Beats 83% in terms of runtime and 59% in
terms of memory.

First time submission succesful.

It took me 1 hour and 12 to come up with this
solution.

Apparently this was a hard problem.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize (node : "TreeNode"):
    queue = list()
    serialized = list()
    
    if node is None:
        return []
    
    queue.append(node)
    index = 0
    queue_length = 1
    while index < queue_length:
        current = queue[index]
        
        if current is not None:
            serialized.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            serialized.append(None)
        
        queue_length = len(queue)
        index += 1
    return serialized

def to_nodes(nodes_list : list) -> list:
    nodes = list()
    for num in nodes_list:
        if num is not None:
            nodes.append(TreeNode(num))
        else:
            nodes.append(None)
    return nodes
            
def deserialize(nodes_list : list) -> "TreeNode":
    if not nodes_list:
        return None
    
    nodes = to_nodes(nodes_list)
    index = 0
    start_children = 1
    total_nodes = len(nodes_list)
    while index < len(nodes_list):
        if nodes_list[index] is not None:
            if start_children < total_nodes:
                nodes[index].left = nodes[start_children]
            if start_children + 1 < total_nodes:
                nodes[index].right = nodes[start_children + 1]
            start_children += 2
            index += 1
        else:
            index += 1
        
    return nodes[0]

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return serialize(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return deserialize(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))