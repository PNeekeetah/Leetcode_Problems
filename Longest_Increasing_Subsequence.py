'''
 # @ Author: Nikita
 # @ Creation Time: 2021-07-09 22:48:23
 # @ Last Modified: 2021-07-10 15:15:22
'''

"""
 Took me way too long (probably 3 hours) and I failed  
 many submissions (probably 5). Beats 47% in terms off 
 memory and 18% in terms of runtime.

 I also cheated and looked for a solution online because 
 I could find no solution of my own try as I might.

 Finally managed to write a Dynamic Programming version 
 - 2021-07-10 
"""

from typing import List, Dict
import random as r

def longest_subsequence(nums : List[int], index : int, sequence_dict : Dict[int,int]) -> int:
    if sequence_dict.get(index) is not None:
        return sequence_dict[index]
    value = 1 
    for i in range(0,index):
        if nums[i] < nums[index]:
            value = max(value, 1 + longest_subsequence(nums,i, sequence_dict))
    sequence_dict[index] = value  
    return value  

class Solution:
    def lengthOfLISDP(self, nums: List[int]) -> int:
        sequence_dict : Dict[int,int] = dict()
        sequence_dict[0] = 1
        max_val = 1
        for j in range(len(nums)):
            max_val = max(max_val, longest_subsequence(nums,j,sequence_dict))
        return max_val

    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        longest_subsequence = [1 for _ in range(len(nums))]

        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    longest_subsequence[i] = max(longest_subsequence[i], longest_subsequence[j] + 1)

        return max(longest_subsequence)
            

"""
For testing purposes
"""

test1 = [10,9,2,5,3,7,101,18,20,13,20]
test2 = [0,1,0,3,2,3]
test3 = [7,7,7,7,7,7,7,7,7,7,7]
testp = [1,2,3,4,3,2,1,2,3,4,4,1,2,3,4,3,5,1,2,3,4,3,6,1,2,3,4,3,7,1,2,3,4,3,8,3,2,9]
test4 = [0,1,0,3,2,3]
test5 = [0,1,2,3,4]
# Random test 
RAND_RANGE = 10
RAND_MAX = 100
RAND_MIN = 0
testr = [r.randint(RAND_MIN,RAND_MAX) for _ in range(RAND_RANGE)]

solution = Solution()
val = solution.lengthOfLISDP(test2)
print(val)

            



