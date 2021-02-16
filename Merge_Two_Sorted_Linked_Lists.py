# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:42:13 2021

@author: Nikita
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def goThrough(self):
        current_node = self
        while not (current_node.next is None):
            print("Node.val = {} ".format(current_node.val) + "Node.next.val = {}".format(current_node.next.val) )
            current_node = current_node.next
        print("\n")
        
class Solution: 
    def __init__(self):
        next
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) and (not l2):
            return None
        elif (not l1):
            return l2
        elif (not l2):
            return l1
        elif (not l1.next) and (not l2.next):
            if (l1.val <= l2.val):
                l1.next = l2
                return l1
            else:
                l2.next = l1
                return l2
        
        first = l1
        second = l2
        new_head = None
        if (l1.val <= l2.val):
            new_head = first
            first = first.next
        else:
            new_head = second
            second = second.next
        current = new_head
    
        while ((first) and (second)):
            if (first.val <= second.val) :
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next
        """
        Not actually needed.
        while first:
            if not(second) or (first.val <= second.val) :
                current.next = first
                first = first.next
            elif (first.val > second.val):
                current.next = second
                second = second.next
            current = current.next
        
        while second :
            if not(first) or (second.val <= first.val) :
                current.next = second
                second = second.next
            elif (second.val > first.val):
                current.next = first
                first = first.next
            current = current.next
        """
        if (first):
            current.next = first
        elif(second):
            current.next = second
    
        return new_head

head1   = ListNode(0)

node_1 = ListNode(1)

node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)

head1.next = node_1

node_1.next = node_2

node_2.next = node_3
node_3.next = node_4        
  
head2   = ListNode(0)
node_5 = ListNode(1)

node_6 = ListNode(2)
node_7 = ListNode(3)
node_8 = ListNode(4)

head2.next = node_5

node_5.next = node_6
node_6.next = node_7
node_7.next = node_8        


solution = Solution()
new_head = solution.mergeTwoLists(head1, head2)
new_head.goThrough()

"""

Admittedly, I butchered this one a bit.
I didn't get it first try, it required multiple code alterations in order
to get it working. 

My idea was essentially this : 
    Go through both lists at the same time and increase one pointer or the
    other, depending on which value is lower. Once a list end is reached, 
    iterate through the remainder of the other list and connect pointers.
    
I had the intuition that iterating through the remainder of the list wouldn't
be needed, but due to how I implemented the code I messed up. 

Anyhow, it took 58 minutes and 38 seconds until I had a working implementation
that I could submit. The first submission on the site was wrong, next one worked.

In terms of speed, the second implementation with the if statement at the end
beats 76.54 % of submissions.
"""