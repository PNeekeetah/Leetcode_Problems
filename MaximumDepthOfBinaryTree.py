# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:51:02 2021

@author: Nikita
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not (root):
            return 0
        
        depth = 1
        queue = []
        queue.append((root,depth))
        current_item = (None,None)
        current_node = None
        max_depth = 1
        while (len(queue) > 0):
            current_item = queue.pop(0)
            depth = current_item[1]
            current_node = current_item[0]
            if (current_node.left):
                queue.append((current_node.left, depth + 1))
                if (depth + 1 > max_depth):
                    max_depth += 1
            if (current_node.right):
                queue.append((current_node.right, depth + 1))
                if (depth + 1 > max_depth):
                    max_depth += 1
        
        return max_depth
    
    def __init__(self):
        self.max_depth = 0
        
    def bestRuntimeSolution(self, root: TreeNode) -> int:
        def advance (node : TreeNode, depth : int) -> int:
            if not (node) :
                return
            
            if not node.left and not node.right:
                self.max_depth = max(depth, self.max_depth)
                return
            
            advance(node.left, depth+1)
            advance(node.right, depth+1)
            
        advance(root,1)
        return self.max_depth
    
    
root = TreeNode(0, None, None)
node1 = TreeNode(1, None, None)
node2 = TreeNode(2, None, None)
node3 = TreeNode(3, None, None)
node4 = TreeNode(4, None, None)
root.left = node1
root.right = node2
node1.left = node3
node3.left = node4

solution = Solution()
print(solution.bestRuntimeSolution(root))
        

"""
The solution i'm thinking of is essentially a depth first search. I don't
dabble too much in recursion, so I will go ahead and implement an iterative
DFS. 

Results : 
    - Succesful submission after 33 minutes and 47 seconds
    - beats 76% in terms of runtime
    - beats 97.45% in terms of memory
    
Interestingly, the best solution does it recursively. I will code the 
best solution in terms of runtime here as well:
    
Now, I tested the best solution in terms of runtime and it's absolutely
junk. It is between 75% and 49% faster than the rest.
It is also memory inefficient, probably due to the calls on the stack.
It feels like it might have been a fluke; oh well.

Nonetheless, I like how elegant it is.

"""