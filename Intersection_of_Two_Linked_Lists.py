# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 00:24:45 2021

@author: Nikita
"""

"""
Did it both with constant memory and O(n) runtime and
with O(n) memory and O(n) runtime.

The O(n) runtime O(1) memory beats 22% in terms of 
runtime and 31% in terms of memory. It took me about
23 minutes to come up with this solution

The O(n) mem O(n) runtime solution beats 76% in terms 
of runtime It took me about 11 minutes to come up
with this solution.

The O(n) runtime O(1) memory failed a test case
the first time because of a badly placed if 
statement

The O(n) runtime O(n) memory got accepted the
first time.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def advance_one(node : "ListNode"):
    if node is not None:
        return node.next
    else:
        return None
    
def get_list_length_and_last_node(node : "ListNode") -> (int,"ListNode"):
    current = node
    length = 0
    last_node = None
    while current is not None:
        if (
            current is not None and 
            current.next is None
        ):
            last_node = current
        length += 1
        current = advance_one(current)
    return (length, last_node)

def set_sail(node : "ListNode", steps : int) -> "ListNode":
    while steps > 0:
        node = advance_one(node)
        steps -= 1
    return node

def advance_two_nodes(nodeA : "ListNode", nodeB : "ListNode") -> ("ListNode","ListNode"):
    nodeA = advance_one(nodeA)
    nodeB = advance_one(nodeB)
    return (nodeA,nodeB)

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        lengthA = 0
        lengthB = 0
        currentA = headA
        currentB = headB
        
        lengthA,currentA = get_list_length_and_last_node(currentA)
        lengthB,currentB = get_list_length_and_last_node(currentB)
        # If they don't end on the same node, they don't intersect
        if currentB != currentA:
            return None
        
        # Set sail to one of the pointers
        difference = lengthA - lengthB
        nodeA = headA
        nodeB = headB
        if difference < 0:
            nodeB = set_sail (nodeB,abs(difference))
        elif difference > 0:
            nodeA = set_sail (nodeA,difference)
        
        # Advance both till equal
        while nodeA != nodeB:
            nodeA,nodeB = advance_two_nodes(nodeA,nodeB)
        else:
            return nodeA
    
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen_set = set()
        currentA = headA
        currentB = headB
        
        # Visit all of A
        while currentA is not None:
            seen_set.add(currentA)
            currentA = advance_one(currentA)
        
        # Start visiting all of B
        # if the node is in the seen set, return
        while currentB is not None:
            if currentB in seen_set:
                return currentB
            else:
                currentB = advance_one(currentB)
        
        # If we get here, they don't intersect
        return None        