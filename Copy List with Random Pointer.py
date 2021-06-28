# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:14:36 2021

@author: Nikita
"""

#htqtps://leetcode.com/problems/copy-list-with-random-pointer/

"""
Updated this solution 
New version beats 92% in terms of runtime and
23% in terms of memory. It took me about 10 
minutes to come up with this solution.

The organization 
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        self.list = []

def advance_one (node : "Node") -> "Node":
    if node.next is not None:
        return node.next
    else:
        return None

def fetch_node (nodes_dict : dict, node : "Node") -> "Node":
    if node in nodes_dict:
        return nodes_dict[node]
    else:
        if node is not None:
            nodes_dict[node] = Node(node.val)
        return nodes_dict.get(node,None)
        
class Solution:
    
    def copyRandomList(self, head: 'Node') -> 'Node':  # Updated solution
        if head is None: 
            return None
        
        nodes_dict = dict()
        current = head
        while current is not None:
            new_node = fetch_node(nodes_dict,current)
            new_node.next = fetch_node(nodes_dict,current.next)
            new_node.random = fetch_node(nodes_dict,current.random)
            current = advance_one(current)
        return nodes_dict[head]
    
    def copyRandomList1(self, head: 'Node') -> 'Node':                
        def deepcopy(head : "Node",explored_nodes :dict() = None):
            new_head = None
            if not explored_nodes:
                explored_nodes = {}
            if (explored_nodes.get(head)):
                return explored_nodes[head]
            if (head):
                new_head = Node(head.val)
                explored_nodes[head] = new_head
                new_head.next = deepcopy(head.next,explored_nodes )
                new_head.random = deepcopy(head.random,explored_nodes )
            return new_head
        return deepcopy(head)



n4 = Node(10,None)
n3 = Node(4211,n4)
n2 = Node(41,n3)
n1 = Node(0,n2)

n1.random = n4
n2.random = n1
n3.random = n2
n4.random = n3

dic = {}
dic[n1] = n2

solution = Solution()
dc = solution.copyRandomList(n1)


"""
It probably took me about 2 hours to get a working version.
I submitted it twice; first, I created an iterative version that assumed
values would be different -> this wasn't the case, and as such it failed
8 test cases.

I created another version which is recursive. It beats 30% in terms of
runtime and 7% in terms of memory. 

The solution uses 2 arrays. The first one keeps track of the exploration of
the first linked list whereas

Edit : i didn't realise that objects in python are hashable; as such, I completely
ignored the possibility of using a dictionary. The dictionary solution beats 99%
in terms of runtime.

# Logic behind iterative version which was wrong
In a first pass, I can:
    Create Node 7, Node 8, Node 5, Node 4
    Know the 7->4, 8->5, 5->4 AND
    know that 7.r.v = 5 (node 0) -> 7,node[0] is connected to node with val (5,0) / what I actually want is 7,0 -> (5,2) / 7->0
              8.r.v = 7 (node 1) -> 8,node[1] is connected to node with val (7,1) / what I actually want is 8,1 -> (7,0) / 8->1
              5.r.v = 7 (node 2) -> 5,node[2] is connected to node with val (7,2) / what I actually want is 5,2 -> (7,0) / 5->2
              4.r.v = 8 (node 3) -> 4,node[3] is connected to node with val (3,3) / what I actually want is 4,3 -> (8,1) / 4->3
              
It doesn't work if there are duplicate values. 
"""
