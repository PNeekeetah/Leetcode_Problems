# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 23:07:21 2021

@author: Nikita
"""

# Definition for a Node.

"""
Took me about 30 minutes to figure this one out.
It's done in O(n) runtime and O(n) memory.

This solution beats 66% in terms of runtime
and 0% in terms of memory.
"""

class ListNode:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def advance_one (node : "ListNode"):
    if node is not None:
        return node.next
    else:
        return None

def traverse_till_last(node : "ListNode"):
    while node is not None and node.next is not None:
        node = advance_one(node)
    return node

def recursive_traversal (current : "ListNode", stack : list = None):
    if stack == None:
        stack = []
    stack.append(current)
    if current.child is not None:
        recursive_traversal(current.child,stack)
    if current.next is not None:
        recursive_traversal(current.next,stack)
    return stack
    
    
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        nodes_list = recursive_traversal(head)
        total_nodes = len(nodes_list)
        for i in range(0,total_nodes-1):
            print("Handling node {}".format(nodes_list[i].val))
            if i == 0:
                if total_nodes >= 2:
                    nodes_list[0].next = nodes_list[1]
                    nodes_list[1].prev = nodes_list[0]
                nodes_list[0].child = None
            else:
                nodes_list[i].next = nodes_list[i+1]
                nodes_list[i+1].prev = nodes_list[i]
                nodes_list[i].child = None
        else:
            print("Handling node {}".format(nodes_list[-1].val))
            nodes_list[-1].child = None
            nodes_list[-1].prev = nodes_list[-2]
        return head
        