# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:16:06 2021

@author: Nikita
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class TreeTraversal:
    def __init__(self):
        self.nodes_list = []
        
    def bfs_iterative (self, node : TreeNode) :
        if not (node):
            return None
        queue = [(node,0)]
        current_node = None
        while (len(queue) > 0 ):
            current_item = queue.pop(0)
            current_node = current_item[0]
            current_depth = current_item[1]
            if (current_node.left):
                queue.append((current_node.left,current_depth+1))
            if(current_node.right):
                queue.append((current_node.right,current_depth+1))
            self.nodes_list.append((current_node,current_depth))

class Solution:
    """
    First submission
    """
    def levelOrderWithClass(self, root: TreeNode) -> list(list()):
        traversal = TreeTraversal()
        traversal.bfs_iterative(root)
        level_order = []
        current_level = -1
        for node in traversal.nodes_list:
            if (node[1] != current_level):
                level_order.append([])
                current_level += 1
            level_order[current_level].append(node[0].val)
            
        return level_order
    
    """
    Second submission
    
    """
    def levelOrder(self, root: TreeNode) -> list(list()):
        if not (root):
            return []
        queue = [(root,0)]
        current_node = None
        level_order = []
        current_level = -1
        while (len(queue) > 0 ):
            current_item = queue.pop(0)
            current_node = current_item[0]
            current_depth = current_item[1]
            if (current_node.left):
                queue.append((current_node.left,current_depth+1))
            if(current_node.right):
                queue.append((current_node.right,current_depth+1))
            if (current_depth != current_level):
                level_order.append([])
                current_level += 1
            level_order[current_depth].append(current_node.val)

        return level_order

root = TreeNode(1, None, None)
node1 = TreeNode(2, None, None)
node2 = TreeNode(3, None, None)
node3 = TreeNode(3, None, None)
node4 = TreeNode(2, None, None)
node5 = TreeNode(3, None, None)
node6 = TreeNode(3, None, None)

root.left = node1
root.right = node4
node1.left = node2
node1.right = node3
node4.left = node5
node4.right= node6

traversal = TreeTraversal()
traversal.bfs_iterative(root)
solution = Solution()
print(solution.levelOrder(None))


"""
for node in traversal.nodes_list:
    print(node[0].val, node[1])



The first thing that comes to mind after seeing what is required is to 
do a breadth first search. 

All of a sudden, after writing a BFS, it seems like it really doesn't matter
what i'm using. It could be a DFS just as well.

Submission in 27 minutes and 01 seconds.
Submission beats 63% of submissions in terms of runtime and
48% in terms of memory 

Rather than doing it through the Tree Traversal class, I could very likely
do it directly within the solution.

The second submission beats 84 % in terms of runtime.
"""