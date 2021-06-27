# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:10:31 2021

@author: Nikita
"""

"""
Took me about 20 minutes to finish this one
My solution beats 55% in terms of runtime and 
42 % in terms of memory.

First submission succesful.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def advance_one(node : "ListNode") -> "ListNode":
    if node is not None:
        return node.next
    else:
        return None

def traverse_both(head1 : "ListNode", head2 : "ListNode") -> "ListNode":
    current1 = head1
    current2 = head2
    while current1 is not None and current2 is not None:
        current1 = advance_one(current1)
        current2 = advance_one(current2)
    if current1 is not None:
        return head1
    else:
        return head2 
    
def add_lists(more_nodes : "ListNode", less_nodes : "ListNode" ) -> "ListNode":
    carry = 0
    current_more = more_nodes
    current_less = less_nodes
    previous_more = None
    # Add the numbers whilst both lists have nodes left
    while current_less is not None:
        operand1 = current_more.val
        operand2 = current_less.val
        current_more.val = (operand1 + operand2 + carry)%10
        carry =  (operand1 + operand2 + carry)//10
        previous_more = current_more
        current_less = advance_one(current_less)
        current_more = advance_one(current_more)
    # Continue adding the carry to the larger list if there is a carry
    while carry != 0 and current_more is not None:
        operand1 = current_more.val
        current_more.val = (operand1 + carry)%10
        carry = (operand1 + carry)//10
        previous_more = current_more
        current_more = advance_one(current_more)
    # In case there's no place to add final carry, create new node
    if carry != 0:
        new_node = ListNode(carry)
        if previous_more is not None:
            previous_more.next = new_node
        
    return more_nodes
        
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        longer_list = traverse_both(l1,l2)
        if longer_list == l1:
            return add_lists(l1,l2)
        else:
            return add_lists(l2,l1)
        
        