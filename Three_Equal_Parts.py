"""
Sadly, this solution wasn't accepted.
Turns out that they aren't looking for... 
well, essentially an O(n^3) solution.

Nonetheless, I think this likely works.
"""


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            for j in range(i+2, len(arr)):
                num1 = int("".join([str(_) for _ in arr[0: i + 1]]), 2)
                num2 = int("".join([str(_) for _ in arr[i + 1: j]]), 2)
                num3 = int("".join([str(_) for _ in arr[j:]]), 2)
                if num1 == num2 and num2 == num3:
                    return [i, j]
        return [-1, -1]
