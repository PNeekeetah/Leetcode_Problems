# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:02:39 2021

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
        
    def reverseList(self, head: ListNode) -> ListNode:
        if not(head):
            return None
        
        elif not (head.next):
            return head
        
        first = head
        second =  head.next
        
        if not (second.next):
            second.next = first
            first.next = None
            return second

        aux_node = second.next
        second.next = first
        first.next = None
        first = second
        second = aux_node
            
        while (second.next):
            aux_node = second.next
            second.next = first
            first = second
            second = aux_node
                        
        second.next = first
        
        return second
    
    def isPalindrome(self, head: ListNode) -> bool:
        # Gets number of nodes
        if (not head):
            return True
        if(not head.next):
            return True
        
        current_node = head
        total_nodes = 0
        while (current_node):
            current_node = current_node.next
            total_nodes += 1
        
        # Iterates halfway through
        current_node = head
        for i in range (total_nodes//2):
            current_node = current_node.next
        
        # Reverse from halway point
        tail_ptr = self.reverseList(current_node)
        head_ptr = head
        
        # Final check
        while (head_ptr and tail_ptr):
            if (head_ptr.val != tail_ptr.val):
                return False
            
            head_ptr = head_ptr.next
            tail_ptr = tail_ptr.next
            
        return True
    
    def isPalindromeBESTSOLUTION(self, head: ListNode) -> bool: # Not implemented by me
        
        if not head or not head.next:
            return True
        
        size = 0
        curr = head
        
        while curr:
            size += 1
            curr  = curr.next
        
        #print(size)
        
        prev = None
        curr = head
        
        i = 0
        while i != size//2:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            i += 1
        first_half_start = prev
        second_half_start = curr
        #print("head",head)
        #print("tail",tail)
        
        if size%2 !=0:
            t = second_half_start.next
            h = first_half_start
        else:
            t = second_half_start
            h = first_half_start
        
        while t and h:
            if t.val != h.val : return False
            t = t.next
            h = h.next
        return True
            
        
head1   = ListNode(0)
node_1 = ListNode(1)
"""
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
"""
head1.next = node_1
"""
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4        
 """
 
solution = Solution()
print(solution.isPalindrome(head1))
"""

First way I can think of doing this problem is by appending all nodes to
a list, then iterating from the start and end and checking. That would 
take up memory though and it ads 1/2O(n) to overall complexity, which
is still O(n) but nonetheless.

Apparently, it can be done in both O(n) complexity and O(1) space (from 
the hint they give out on the website).

Well, the only way I can think of with regards to how you could check
if the linked list is a palindrom is as follows:
    
1. iterate once through the entire list to find out how many links there 
are.
2. iterate through half of the links (if the links are even) or half + 1 (links
are odd), and from that point on reverse all links.
3. iterate once again with one pointer from the end and one pointer from 
the beginning and if it breaks once, return False/ otherwise, True.
 
I will cheat and use the Reverse Linked List i used a priori.

It works with a list such as 0 -> 1 -> 2 -> 1 -> 0 without a hitch
It also works with a list such as 0-> 1 -> 1 -> 0
It also works with a list such as 0 -> 0

This leaves the only the following 2 edge cases then:
    1: no nodes in the list
    2: only one node
    
Return True if this case is encountered.

Final :
    
It took me 49 minutes and 13 seconds to submit this solution succesfully.
I would be lying if I said that I didn't test the build incrementally.
First time I ran the code online, it failed because of an improperly 
set condition.Otherwise, the first time I submitted it was succesful. 
My solution beat 78% of the other solutions in terms of runtime and 
it beat 79% in terms of memory allocation.

The best solution in terms of runtime implemented the same idea, but they
dint't execute the second step. You can reverse the first half directly, then
compare it against the second one from the current node. This saves n/2 
operations.

"""