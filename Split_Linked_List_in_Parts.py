# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 16:40:21 2021

@author: Nikita
"""

"""
Took me 21 minutes and 36 to solve this problem.
It beats 82.31% in terms of runtime and 14.63% in 
terms of memory.

First submission succesful.
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def advance_one(node : "ListNode") -> "ListNode":
    if node is not None:
        return node.next
    else:
        return None

def count_nodes (node : "ListNode") -> int:
    count = 0
    if node is None:
        return 0
    else:
        while node is not None:
            count += 1
            node = advance_one(node)
    return count
        
def divide (nodes : int, split : int) -> list:
    split_ways = [nodes//split for i in range(split)]
    remainder = nodes - nodes//split*split
    index = 0
    while remainder > 0:
        split_ways[index] += 1
        remainder -= 1
        index += 1
    return split_ways

def get_next(node :"ListNode") -> "ListNode":
    if node is not None and node.next is not None:
        return node.next
    else:
        return None

def traverse (node : "ListNode", nodes_number : int) -> "ListNode":
    current = node
    nodes_number -= 1
    while nodes_number > 0:
        current = advance_one(current)
        nodes_number -= 1
    return current

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list("ListNode"):
        total_nodes = count_nodes(head)
        lists = []
        split_ways = divide(total_nodes,k)
        current = head
        for i,number in enumerate(split_ways):
            lists.append(current)    
            current = traverse(current, number)
            next_node =  get_next(current)
            if current is not None:
                current.next = None
            current = next_node
        return lists
                