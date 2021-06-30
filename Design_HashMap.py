# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:50:18 2021

@author: Nikita
"""

"""
Runtime beats 42% of submissions
Memory usage beats 34% of submissions

O(n) lookup can be reduced to O(log(n))
average time with an AVL tree, but no
idea how to implement that as of yet.

I cheated because I copied my HashSet 
implementation, yet it still took me
13 minutes to figure out what to change
to make it run. 

"""

class ListNode:
    def __init__(
        self,
        key : int,
        value : int, 
        next_node : "ListNode" = None
    ):
        self.key = key
        self.value = value
        self.next = next_node
        
    def get_key(self):
        return self.key

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def set_next(self, next_node : "ListNode"):
        self.next = next_node
    
    def set_value(self, value : int):
        self.value = value
  
def advance_one(node : "ListNode"):
    if node is not None:
        return node.next
    else:
        return None
    
def find (head : "ListNode", key : int):
    current = head
    previous = None
    found = False
    while current is not None:
        if current.get_key() == key:
            found = True
            break
        previous = current
        current = advance_one(current)
    return found, previous, current

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_size = 500
        self.hash_arr = [ListNode("start","start") for i in range(self.bucket_size)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = key % self.bucket_size
        found, _, current = find(self.hash_arr[bucket],key)
        
        if found:
            current.set_value(value)
            return 
        
        start_node = self.hash_arr[bucket]
        new_node = ListNode(key,value)

        if start_node.next is not None:    
            new_node.set_next(start_node.next)

        start_node.set_next(new_node)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = key % self.bucket_size
        found, _ , current = find(self.hash_arr[bucket],key)
        
        value = -1
        if found:
            value = current.get_value()
            
        return value

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = key % self.bucket_size
        found, previous, current = find(self.hash_arr[bucket],key)
        
        if not found:
            return
        
        previous.set_next(current.get_next())
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)