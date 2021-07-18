"""
Beats 66% in terms of runtime
Beats 17% in terms of memory

Took me about 20 minutes to 
come up with this

First time submission failed 
because I forgot to check 
whether the state already
existed in the queue
"""


def generate_squares(n: int):
    number = 1
    squares = list()
    while number**2 <= n:
        squares.append(number**2)
        number += 1
    return squares


class Solution:
    def numSquares(self, n: int) -> int:
        squares = generate_squares(n)
        queue = [(0, 0)]
        index = 0
        seen_set = {0}

        if n in squares:
            return 1

        while index < len(queue):
            current, level = queue[index]

            if current == n:
                return level

            for sqr in squares:
                val = current + sqr
                if val <= n and val not in seen_set:
                    queue.append((val, level+1))
                    seen_set.add(val)

            index += 1
