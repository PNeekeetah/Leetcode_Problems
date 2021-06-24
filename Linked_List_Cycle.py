# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:50:50 2021

@author: Nikita
"""

def advance_one (node):
    if node is not None:
        node = node.next
    else:
        return None
    return node
    
def advance_two (node):
    for i in range(2):
        node = advance_one (node)
    return node

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
    def hasCycle(self, head: ListNode) -> bool:
        fast_node = head
        slow_node = head
        while True:
            fast_node = advance_two(fast_node)
            slow_node = advance_one(slow_node)
            if fast_node == slow_node:
                break
                
        return fast_node is not None

    
    def hasCycle1(self, head: ListNode) -> bool:
        current_node = head
        while (current_node):
            if (current_node.next) and (current_node.next.next):
                if (current_node is current_node.next) or (current_node is current_node.next.next):
                    return True    
                current_node.next = current_node.next.next
                current_node = current_node.next
            else : 
                break
            
            
        return False
    
head   = ListNode(3)
node_1 = ListNode(2)
node_2 = ListNode(0)
node_3 = ListNode(-4)
#node_4 = ListNode(4)
head.next = node_1
node_1.next = head
node_2.next = node_3
#node_3.next = node_1
#node_4.next = head

solution = Solution()
print(solution.hasCycle(head))

"""

So, in this particular case, I am actually quite proud of the solution I came
up with. 

- First submission accepted
- 48 minutes and 11 seconds to come up with a solution that
a) Beats 99.38% (almost 3 sigma!!) in terms of memory usage and 
b) Beats 41% in terms of Runtime ( :( )

My solution essentially revolves around "Crunching" up the list. If at
any the next or next.next value is None, you instantly break because
you know there's no cycle -> you know the list has no cycle

Otherwise, continue "crunching" up the list (by crunching I mean deleting every
2nd node) until you reach a) 2 nodes that circle each other or b) 1 node.
You can return True in this case, because that unique node / those 2 nodes are
the "compressed" version of the cycle. -> Return false.

I will read about memory and Runtime tomorrow.

"""
