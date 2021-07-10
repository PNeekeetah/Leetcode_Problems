'''
 # @ Author: Nikita
 # @ Creation Time: 2021-07-09 22:48:23
 # @ Last Modified: 2021-07-10 02:03:26
 '''

 """
 Took me way too long (probably 3 hours) and I failed  
 many submissions (probably 5). Beats 47% in terms off 
 memory and 18% in terms of runtime.

 I also cheated and looked for a solution online because 
 I could find no solution of my own try as I might.
 """

class Solution:
    def lengthOfLIS(self, nums: t.List[int]) -> int:
        if nums == []:
            return 0

        longest_subsequence = [1 for i in range(len(nums))]

        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    longest_subsequence[i] = max(longest_subsequence[i], longest_subsequence[j] + 1)

        return max(longest_subsequence)
            

"""
For testing purposes
"""
import typing as t
import random as r

test1 = [10,9,2,5,3,7,101,18,20,13,20]
test2 = [0,1,0,3,2,3]
test3 = [7,7,7,7,7,7,7,7,7,7,7]
testp = [1,2,3,4,3,2,1,2,3,4,4,1,2,3,4,3,5,1,2,3,4,3,6,1,2,3,4,3,7,1,2,3,4,3,8,3,2,9]
test4 = [0,1,0,3,2,3]
# Random test 
RAND_RANGE = 10
RAND_MAX = 100
RAND_MIN = 0
testr = [r.randint(RAND_MIN,RAND_MAX) for _ in range(RAND_RANGE)]
            



