# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 18:36:25 2021

@author: Nikita
"""

"""
Beats 89% in terms of runtime and 23% in terms of memory.
First time submission succesful.
Took me about 20 minutes to come up with this.
""" 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def advance_one (node : "ListNode"):
    if node is not None:
        return node.next
    else:
        return None
    
def remove_nodes_with_value (
    previous : "ListNode",
    current : "ListNode", 
    value : int,
) -> "ListNode":
    # Skip over all nodes with <value>
    while current is not None and current.val == value:
        current = advance_one(current)
    if previous is not None:
        previous.next = current
    return current
    

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = head
        previous = None
        while current is not None:
            if current.val == val:
                if current == head:
                    head = remove_nodes_with_value (
                        previous ,
                        current , 
                        val ,
                    )
                else:
                    current = remove_nodes_with_value (
                        previous ,
                        current , 
                        val ,
                    )
            previous = current
            current = advance_one(current)    
            
        return head
            
            