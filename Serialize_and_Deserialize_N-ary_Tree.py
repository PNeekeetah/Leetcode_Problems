from typing import List, Tuple
from random import randint

"""
Took me about 10 minutes to design serialization
and deserialization. Took me another 20 minutes 
to design a fuzzy test.

I don't know how it compares against the other 
solutions since I don't have leetcode premium
and I can't submit it. It seems to pass all the 
random tests (tested it for trees ranging from
0 to 100 nodes up to 100000 times)

The idea is to perform a BFS and append node
values in the order in which they appear.

Each node value is accompanied by the number 
of children it has. i.e.

[(1,3),(2,0),(3,0),(4,1),(5,0)]. This denotes
the N-ary tree

        1
  ______|_______
  |     |      |
  |     |      |
  2     3      4
               |
               |
               5
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        if children is None:
            self.children = list()
        else:
            self.children = children


def serialize_n_ary_tree(root: "Node"):
    queue = [root]
    serialized = list()
    index = 0
    while index < len(queue):
        current = queue[index]
        queue.extend(current.children)
        serialized.append((current.val, len(current.children)))
        index += 1
    return serialized


def create_nodes(serialized_tree: List[Tuple[int, int]]) -> List["Node"]:
    return [Node(val[0]) for val in serialized_tree]


def deserialize_n_ary_tree(serialized_tree: List[Tuple[int, int]]) -> "Node":
    if len(serialized_tree) == 0:
        return None
    queue = create_nodes(serialized_tree)
    index = 0
    children_start = 1
    while index < len(queue):
        current = queue[index]
        children_no = serialized_tree[index][1]
        children_range = range(
            children_start,
            children_start + children_no
        )
        for j in children_range:
            current.children.append(queue[j])
        children_start += children_no
        index += 1
    return queue[0]


def create_n_ary_tree_serialization():
    overal_nodes = randint(1, 10000)
    overal_children = overal_nodes - 1
    nodes = []
    for i in range(overal_nodes):
        children = 0
        if overal_children > 0:
            children = randint(1, overal_children)
        overal_children -= children
        nodes.append((i, children))
    return nodes


serialized_tree = [(1, 3), (2, 1), (3, 0), (4, 1), (5, 0), (6, 0)]
"""
print(
    serialize_n_ary_tree(
        deserialize_n_ary_tree(
            serialized_tree
        )
    ) == serialized_tree
)
"""
exceptions = 0
for i in range(1000):
    serialized = create_n_ary_tree_serialization()
    try:
        assert(
            serialize_n_ary_tree(
                deserialize_n_ary_tree(
                    serialized
                )
            ) == serialized
        )
    except Exception as e:
        print(serialized)
        print(e)
        print()
        exceptions += 1

print("Overall exceptions:", exceptions)
