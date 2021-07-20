from typing import List
"""
First solution is a brute force approach.
It fails Leetcode's time limit.

Interestingly, the list comprehension one
which has only 1 branch is even slower 
than a normal for loop.
"""


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        template = "{number:0>{length}}"
        num_template = "{:sign}{:number}"
        total = 0

        for i in range(2**length):
            symbols = template.format(number=bin(i)[2:], length=length)
            accumulator = sum(
                [
                    int(
                        num_template.format(
                            ("+" if s == "1" else "-"),
                            num
                        )
                    ) for s, num in zip(symbols, nums)
                ]
            )
            total += accumulator == target

        return total
