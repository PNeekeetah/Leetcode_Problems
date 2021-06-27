# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:44:36 2021

@author: Nikita
"""

"""
This beats 64% in terms of runtime and 16% in terms of 
memory. The requirement though was constant memory, so
let's try again, this time with constant memory.

I'll admit, it wasn't immediately obvious to me how i'd
do it with constant memory. I looked at a solution 
and I got inspired to create auxiliary ListNodes to use
as heads. Although I cheated a bit, the rest of the
solution is my onw. I'll just mark the 2 bits
I used as inspiration with 2 # comments


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

def assemble_list(array : list) -> ("ListNode","ListNode"):
    for i in range (len(array)-1):
        array[i].next = array[i+1]
    if array != []:
        array[-1].next = None
        return (array[0],array[-1])
    else:
        return None, None
    
class Solution:
    
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = ListNode("odd")      #inspiration1
        even_head = ListNode("even")    #inspiration2
        current = head
        current_odd = odd_head
        current_even = even_head
        is_odd = True
        
        while current is not None:
            if is_odd:
                current_odd.next = current
                current_odd = advance_one(current_odd)
            else:
                current_even.next = current
                current_even = advance_one(current_even)
            is_odd = not is_odd
            current = advance_one(current)
        
        odd_head = advance_one(odd_head)
        even_head = advance_one(even_head)
        
        current_odd.next = even_head
        current_even.next = None
        
        return odd_head
    
    def oddEvenList1(self, head: ListNode) -> ListNode:
        odd_list = list()
        even_list = list()
        current = head
        current_counter = 1
        
        # Alternate putting each element into an array
        while current is not None:
            if current_counter % 2 == 0:
                even_list.append(current)
            else:
                odd_list.append(current)
            current_counter += 1
            current = advance_one(current)
        
        # Recreate the 2 linked lists
        odd_head,odd_last = assemble_list(odd_list)
        even_head, even_last = assemble_list(even_list)
        
        # Assemble the final linked list
        if odd_last is not None:
            odd_last.next = even_head
            return odd_head
        else:
            return even_head
        