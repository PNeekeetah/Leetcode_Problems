

"""
Beats 13% in terms of runtime and 0%
in terms of memory usage.

Took me 5 minutes to come up with this.
First submission succesful.
"""
# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def bfs_max_level(root: "Node") -> int:
    if root is None:
        return 0

    queue = [(root, 1)]
    index = 0
    max_level = 0
    while index < len(queue):
        current, level = queue[index]
        for child in current.children:
            queue.append((child, level+1))
        max_level = max(max_level, level)
        index += 1
    return max_level


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return bfs_max_level(root)
