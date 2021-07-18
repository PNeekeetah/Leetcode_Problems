"""
Beats 59% in terms of runtime and 0%
in terms of memory.

I had an idea how to do it recursively,
but no idea how to do it via DFS. Second
submission was succesful because I didn't
take into account what would happen for 
an empty graph.

I was supposed to solve it with a stack,
but I solved it with a queue.
"""

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen_nodes = dict()
        queue = list([node])
        index = 0
        if node == None:
            return None
        while index < len(queue):
            current = queue[index]
            seen_nodes.setdefault(current, Node(current.val))
            for node in current.neighbors:
                if node not in seen_nodes:
                    queue.append(node)
                seen_nodes.setdefault(node, Node(node.val))
                seen_nodes[current].neighbors.append(seen_nodes[node])
            index += 1
        return seen_nodes[queue[0]]
