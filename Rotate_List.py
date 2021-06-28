# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:34:04 2021

@author: Nikita
"""

"""
The design didn't really take me that long/ however, accounting 
for edge cases did. Took me 30 minutes overall to submit a 
succesful piece of code

Runtime : beats 52% of submissions  
Memory : beats 59% of submissions

4th attempt succesful since I messed up edge cases.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def advance_one (node : "ListNode") -> "ListNode":
    if node is not None:
        return node.next
    else:
        return None

def get_list_length (head : "ListNode") -> int :
    if head is None:
        return 0
    node = head
    length = 1
    while node is not None and node.next is not None:
        node = advance_one(node)
        length += 1
        
    return length

def get_rotation(total_nodes : int, rotation : int) -> int:
    if total_nodes > 0:
        return rotation % total_nodes
    else: 
        return 0
    return  

def get_linked_list_portion (head : "ListNode", nodes : int) -> ("ListNode","ListNode"):
    if nodes == 0:
        return (head, None)
    
    links = nodes - 1
    current = head
    sentinel = head
        
    while links > 0 and sentinel is not None:
        sentinel = advance_one(sentinel)
        links -= 1
    
    previous = None
    
    while sentinel is not None and sentinel.next is not None:
        previous = current
        current = advance_one(current)
        sentinel = advance_one(sentinel)
    
    if previous is not None:
        previous.next = None
    
    return (current, sentinel)

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        list_length = get_list_length(head)
        rotation = get_rotation(list_length, k)
        new_head, node = get_linked_list_portion(head,rotation)
        if node is not None and new_head != node:
            node.next = head
        elif node is not None and new_head == node:
            new_head.next= head
        return new_head
        