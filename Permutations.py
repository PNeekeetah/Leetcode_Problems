from typing import List, Set

"""
I finished this problem in about 40  minutes .
My solution beats 98% in terms of runtime and 
87% in terms of memory.

Python3 on leetcode is on version 3.9. Mine
is 3.7. This code  runs in my version, but
doesn't on 3.9 presumably due to the fact
that my solution is a bit hacky. 

I decided  to use Python 2.7 to submit this
since I assumed it'll work - it did.
"""

def recurse(nums_set : Set[int], partial_solution : List[int], solution : List[List[int]]):
    if len(nums_set) ==  0:
        return True
    
    local_set = set(nums_set)
    """
    This is more insidious than it seems. If we iterate directly 
    over nums_set, we end up re-adding the same list of elements 
    to the list. 
    """
    for number in local_set:
        partial_solution.append(number)
        local_set.remove(number)
        if recurse(local_set,partial_solution, solution):
            solution.append(list(partial_solution))
        local_set.add(number)
        partial_solution.pop()
    
    return False
    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        partial_solution : List[int] = list()
        solution : List[List[int]] = list()
        """
        We convert "nums" to a set because sets support
        adding and removing elements, which is probably
        O(1). For a list, i'd have to insert which is O(n)
        """
        recurse(set(nums),partial_solution,solution)
        return solution

solution = Solution()
nums = solution.permute([1])
print(nums)