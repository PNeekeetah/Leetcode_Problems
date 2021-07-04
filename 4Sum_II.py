# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 01:30:37 2021

@author: Nikita
"""

"""
Beats 13% in terms of runtime and 0% in terms of memory.

I went down from an O(n^4) solution to an O(n^2) solution,
but sadly I didn't realise I didn't need to use that much
memory and it failed due to running out of memory.

Technically, first submission would have been succesful
if leetcode wasn't so whyny about its memory usage and 
time limits :/

Nonetheless, the O(n^2) solution seems to be the fastest
one.
""" 

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        tuples_dict = dict()
        total_tuples = 0
        
        for i,number1 in enumerate(nums1):
            for j,number2 in enumerate(nums2):
                tuples_dict.setdefault(number1 + number2, []).append((i,j))

        for k,number3 in enumerate(nums3):
            for l,number4 in enumerate(nums4):
                tuples = tuples_dict.get(-number3 - number4)
                if tuples is not None:
                    total_tuples += len(tuples)
                        
        return total_tuples
    
"""
Attempts : 
"""

def fourSumCount(nums1, nums2, nums3, nums4) -> int:
        
        tuples = []
        total = len(nums1)
        for i in range(total):
            for j in range(total):
                for k in range(total):
                    for l in range(total):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:  
                            tuples.append((i,j,k,l))
        
        return len(tuples)
    
def fourSumCount2(nums1,nums2,nums3,nums4) -> int:
    tuples_dict = dict()
    tuples_list = list()
    
    for i,number1 in enumerate(nums1):
        for j,number2 in enumerate(nums2):
            tuples_dict.setdefault(number1 + number2, []).append((i,j))
            
    for k,number3 in enumerate(nums3):
        for l,number4 in enumerate(nums4):
            tuples = tuples_dict.get(-number3 - number4)
            if tuples is not None:
                for tup in tuples:
                    i,j = tup
                    tuples_list.append((i,j,k,l))
    
    return len(tuples_list)

def fourSumCount3(nums1,nums2,nums3,nums4):
    

import random

trials = 100
numbers = 1
succesful_trials = 0
r = 1
for j in range(trials):
    nums1 = [random.randint(-r,r) for i in range(numbers) ]
    nums2 = [random.randint(-r,r) for i in range(numbers) ]
    nums3 = [random.randint(-r,r) for i in range(numbers) ]
    nums4 = [random.randint(-r,r) for i in range(numbers) ]
    result1 = fourSumCount(nums1,nums2,nums3,nums4)
    result2 = fourSumCount2(nums1,nums2,nums3,nums4)
    if result1 == result2:
        print("Same result for trial {} | {}".format(j+1,result1))
        succesful_trials += 1
        
        
print(succesful_trials)