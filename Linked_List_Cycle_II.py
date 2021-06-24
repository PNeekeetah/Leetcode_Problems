# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:26:45 2021

@author: Nikita
"""

""" LEETCODE SOLUTION DOWN BELOW
Commented this out because the code i'm actually interested in running
is below this comment block

Took me about an hour of head scratching/ first submission was succesful and
it beats 22% in terms of memory. It's done in place. 

I'm aware I could have used a set and I could have advanced one node 
continuously, but i wanted to do it in O(n) runtime and O(1) memory.

I did it with O(n) memory as well and now it beats 31.29% in terms of runtime
and 17.81 % in terms of runtime. It took me about 5 minutes to code it.

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

class Solution:
    
    def detectCycle(self, head: ListNode): # second solution
        nodes_set = {}
        current = head
        while current is not None and current not in nodes_set:
            nodes_set.add(current)
            current = advance_one(current)
        return current
    
    def detectCycle2(self, head: ListNode) -> bool: # first solution
        fast_node = head
        slow_node = head
        while True:
            fast_node = advance_two(fast_node)
            slow_node = advance_one(slow_node)
            if fast_node == slow_node:
                break
                
        if fast_node is None:
            return None
        
        cycle_iterations = 0
        while True:
            fast_node = advance_two(fast_node)
            slow_node = advance_one(slow_node)
            if fast_node == slow_node:
                break
            cycle_iterations += 1

        sentinel = head
        for i in range (cycle_iterations+1):
            sentinel = advance_one(sentinel)
        current = head
        while sentinel != current:
            sentinel = advance_one(sentinel)
            current = advance_one(current)
        
        return sentinel
        
"""

import matplotlib.pyplot as plt

total_iterations_arr = []
to_find_iterations_arr = []
cycle_iterations_arr = []


def advance_one(node : "ListNode") -> "ListNode":
    if node is not None:
        return node.next
    else:
        return None

def advance_two(node : "ListNode") -> "ListNode":
    for count in range(2):
        node = advance_one(node)
    return node

def convert_list_to_linked(array_in : list) -> "ListNode":
    if not array_in:
        return None
    else:
        head = ListNode(array_in[0])
        node = head
        for i in range(1,len(array_in)):
            node.set_next(ListNode(array_in[i]))
            node = node.get_next()
        return head
            
def traverse_linked_list(head : "ListNode") -> None:
    node = head
    while node:
        print (node)
        node = advance_one(node)
        
def add_cycle(head : "ListNode", list_length : int, tap : int) -> None:
    aux_node = None
    current = head
    for i in range(list_length-1):
        if i == tap:
            aux_node = current
        current = advance_one(current)
    current.next = aux_node        
    
def cycle_exists(head : "ListNode") -> bool:
    iterations = 0
    fast_node = head
    slow_node = head
    while True:
        fast_node = advance_two(fast_node)
        slow_node = advance_one(slow_node)
        if fast_node == slow_node:
            break
        iterations += 1
    print("Iterations it took to find cycle : {}".format(iterations))
    
    return fast_node is not None

def cycle_exists2(head : "ListNode") -> bool:
    global total_iterations, to_find_iterations, cycle_iterations 
    iterations = 0
    fast_node = head
    slow_node = head
    while True:
        fast_node = advance_two(fast_node)
        slow_node = advance_one(slow_node)
        if fast_node == slow_node:
            break
        iterations += 1
        
    cycle_iterations = 0
    while True:
        fast_node = advance_two(fast_node)
        slow_node = advance_one(slow_node)
        if fast_node == slow_node:
            break
        iterations += 1
        cycle_iterations += 1
    print("Current node is                  : {}".format(slow_node.__str__()))    
    print("Total iterations                 : {}".format(iterations))
    print("Iterations it took to find cycle : {}".format(
            iterations - cycle_iterations
        )
    )
    print("Cycle iterations  for cycle      : {}\n".format(cycle_iterations))
    total_iterations_arr.append(iterations)
    to_find_iterations_arr.append(iterations - cycle_iterations) 
    cycle_iterations_arr.append(cycle_iterations)
    return fast_node is not None

def cycle_node (head : "ListNode") -> "ListNode":
    fast_node = head
    slow_node = head
    # Asserts existence of cycle
    while True:
        fast_node = advance_two(fast_node)
        slow_node = advance_one(slow_node)
        if fast_node == slow_node:
            break
    
    if fast_node is None:
        return None
    
    # Finds cycle length
    cycle_iterations = 0
    while True:
        fast_node = advance_two(fast_node)
        slow_node = advance_one(slow_node)
        if fast_node == slow_node:
            break
        cycle_iterations += 1
    
    # Sails one node ahead
    sentinel = head
    for i in range (cycle_iterations+1):
        sentinel = sentinel.get_next()
    current = head
    
    # Place where nodes clash again is fault node
    while sentinel != current:
        sentinel = advance_one(sentinel)
        current = advance_one(current)
        
    return sentinel

def cycle_node_2(head : "ListNode") -> "ListNode":
    nodes_set = {}
    current = head
    while current is not None and current not in nodes_set:
        nodes_set.add(current)
        current = advance_one(current)
    return current

def get_last_node(node : "ListNode") -> "ListNode":
    if node is None:
        return None
    
    while node.next: 
        node = advance_one(node)
    
    return node


class ListNode:
    def __init__(
            self, 
            val : int, 
            next_node : "ListNode" = None
    ) -> None:
        self.val = val
        self.next = next_node
        
    def __str__(self):
        return "|{}|".format(self.val)
    
    def get_next(self) -> "ListNode":
        return self.next

    def get_val(self) -> int:
        return self.val
    
    def set_next (
            self,
            next_node : "ListNode"
    ) -> None:
        self.next = next_node

min_node = 1
max_node = 100
array = [i for i in range(min_node,max_node+1)]
head = convert_list_to_linked(array)
last = get_last_node(head)

for i in range (len(array)):
    last.next = None    
    list_element = i
    add_cycle(head,len(array),list_element)
    print("Connected to node {}".format(i))
    cycle_exists2(head)
 
last.next = None    
add_cycle(head,len(array),99)

node = cycle_node(head)
print("Cycle node is " + node.__str__())

plt.plot(array,total_iterations_arr, color="r")
plt.plot(array,to_find_iterations_arr, color="g")
plt.plot(array,cycle_iterations_arr, color = "b")
# cycle_iterations_arr effectively cycle_length


    