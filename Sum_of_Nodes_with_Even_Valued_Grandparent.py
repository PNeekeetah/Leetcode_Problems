# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:11:19 2021

@author: Nikita
"""

"""
Beats 7% in terms of runtime and 41% in terms of memory.
First time submission in 35 minutes because of silly error.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodes_sum = 0
        def inorder(node: TreeNode):
            if not node:
                return
            print(node.val)
            if node.val%2==0:
                go2Deep(node)
            if node.left:
                inorder(node.left)
            if node.right:
                inorder(node.right)
        def go2Deep(node: TreeNode, levels = 2):
            nonlocal nodes_sum
            if levels == 0 and node:
                print("Adding {}".format(node.val))
                nodes_sum += node.val
            if node.left:
                go2Deep(node.left, levels - 1)
            if node.right:
                go2Deep(node.right, levels - 1)
        inorder(root)
        return nodes_sum
    
solution = Solution()
root = TreeNode(6, None, None)
node1 = TreeNode(7, None, None)
node2 = TreeNode(2, None, None)
node3 = TreeNode(7, None, None)
node4 = TreeNode(8, None, None)
node5 = TreeNode(1, None, None)
node6 = TreeNode(3, None, None)
node7 = TreeNode(9)
node8 = TreeNode(1)
node9 = TreeNode(4)
node10 = TreeNode(5)

root.left = node1
root.right = node4

node1.left = node2
node1.right = node3

node4.left = node5
node4.right= node6

node2.left = node7
node3.left = node8
node3.right = node9
node6.right = node10

zzzz = solution.sumEvenGrandparent(root)


    
