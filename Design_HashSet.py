# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:00:41 2021

@author: Nikita
"""

"""
Beats 9% in terms of runtime and 0% 
in terms of memory. 

Took me about 5 minutes to come up 
with this. 

I tried again, this time using a Linked List

it beats 44 % in terms of runtime and 32% in
terms of memory.

Only 1 bucket is not enough
2 buckets neither

anything over 500 seems to do the trick,
but too many buckets makes it run slower 
since we initialize more nodes.

"""

class ListNode:
    def __init__(self, value : int, next_node : "ListNode" = None):
        self.value = value
        self.next = next_node
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node : "ListNode"):
        self.next = next_node
        
    def get_value(self):
        return self.value
    
    def __str__(self):
        node_val = self.val
        next_val = None
        if self.next is not None:
            next_val = self.next.val
            
        return "|{}| -> |{}|".format(node_val, next_val)

def advance_one(node : "ListNode"):
    if node is not None:
        return node.next
    else:
        return None
    
def find (head : "ListNode", value : int):
    current = head
    previous = None
    found = False
    while current is not None:
        if current.get_value() == value:
            found = True
            break
        previous = current
        current = advance_one(current)
    return found, previous, current
    
class MyHashSet1:   # Second Attempt

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_arr = [ListNode("start") for i in range(10**3)]
        

    def add(self, key: int) -> None:
        bucket = key % 1000
        found, previous, current = find(self.hash_arr[bucket],key)
        
        if found:
            return
        
        start_node = self.hash_arr[bucket]
        if start_node.next is not None:
            new_node = ListNode(key)
            new_node.set_next(start_node.next)
            start_node.set_next(new_node)
        else:
            start_node.set_next(ListNode(key))
        
        

    def remove(self, key: int) -> None:
        bucket = key % 1000
        found, previous, current = find(self.hash_arr[bucket],key)
        
        if not found:
            return
        
        previous.set_next(current.get_next())
        
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket = key % 1000
        found, previous, current = find(self.hash_arr[bucket],key)
        
        return found

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_arr = [0 for i in range(10**6+1)]
        

    def add(self, key: int) -> None:
        if self.hash_arr[key] < 1: 
            self.hash_arr[key] += 1
        

    def remove(self, key: int) -> None:
        if self.hash_arr[key] > 0:
            self.hash_arr[key] -= 1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hash_arr[key] == 1