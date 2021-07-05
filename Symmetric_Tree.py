# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:47:39 2021

@author: Nikita
"""

"""
This solution beats 82% in terms of runtime and 51%
in terms of memoyr.

I find this a bit more intuitive than what I've written previously.

The idea is to create a string representation of the binary tree.
The left side is mirrored, meaning that the nodes are swapped
when passed into the recursive function.

Comparing the keys formed in this way yields the final answer.

Second time submission succes
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_dfs_key(node, direction : str = "l", level : int = 0, mirror : bool = False) -> str:
    if node is None:
        return ""
    
    node_left = node.left
    node_right = node.right
    if mirror:
        node_left = node.right
        node_right = node.left
    
    string = str(node.val) + str(level) + direction
    if node_left is not None:
        string += get_dfs_key(node_left, "l", level + 1 , mirror)
    
    if node_right is not None:
        string += get_dfs_key(node_right, "r", level + 1 , mirror)

    return string

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        string1 = get_dfs_key(root.left, "l", mirror = False)
        string2 = get_dfs_key(root.right, "l", mirror = True)

        return string1 == string2
        
"""
Older solution below
"""

class TreeTraversal:
    def __init__(self):
        self.nodes_list = []
        
    # Left, Node, Right
    def dfs_inorder(self, node: TreeNode, direction : str):
        if (node.left):
            self.dfs_inorder(node.left,"L")
        self.nodes_list.append((node,direction))
        if(node.right):
            self.dfs_inorder(node.right,"R")
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not(root):
            return True
        
        traversal = TreeTraversal()
        traversal.dfs_inorder(root,"C")
        
        for node in traversal.nodes_list : 
            print(node[0].val, node[1])

        total_nodes = len(traversal.nodes_list)
        if not(total_nodes % 2):
            return False
        p1 = total_nodes//2 - 1
        p2 = total_nodes//2 + 1
        
        for i in range (total_nodes//2):
            if ((traversal.nodes_list[p1-i][1] == traversal.nodes_list[p2+i][1]) or
               (traversal.nodes_list[p1-i][0].val != traversal.nodes_list[p2+i][0].val)):
                return False
            
        return True
            
        
root = TreeNode(1, None, None)
node1 = TreeNode(2, None, None)
node2 = TreeNode(3, None, None)
node3 = TreeNode(4, None, None)
node4 = TreeNode(2, None, None)
node5 = TreeNode(4, None, None)
node6 = TreeNode(3, None, None)

root.left = node1
root.right = node4

node1.left = node2
node1.right = node3

node4.left = node5
node4.right= node6

traversal = TreeTraversal()
traversal.dfs_inorder(root,"C")
for node in traversal.nodes_list:
    print (node[0].val , node[1] )
    

    
# for 7 nodes, pointer 1 at 2 and pointer 2 at 4
# for 9 nodes, pointer 1 at 3 and pointer 2 at 5
# general rule is len(traversal.nodes) // 2 - 1 and //2 +1 

"""
The idea behind my program is to perform and inorder traversal,
then check that the left half of the nodes' values mirrors the
right half. Theoretically, good idea.

Practically, a case such as 
        1
       / \
      2   2
     /   /
   2    2

this one fails.    

After 3 more failed submissions, I finally got a great idea. 
Why not append the node in the list together with its direction
 Left , Center or Right. It took me 37 minutes and 02 seconds
 to come up with the succesful submission.
 
The final code beats 82% of submissions in terms of runtime, 
and 47% in terms of memory. 

"""