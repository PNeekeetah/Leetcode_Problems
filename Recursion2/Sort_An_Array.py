# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:22:34 2021

@author: Nikita
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(numbers : list()):
            length = len(numbers)
            if (length == 1):
                return numbers
            left  = divide(numbers[0 : length//2])
            right = divide(numbers[length//2 : ])
            return merge (left, right) 
        
        def merge(list1 : list, list2 : list):
            p1 = p2 = 0
            length1 = len(list1)
            length2 = len(list2)
            merged = []
            while (p1 != length1) and (p2 != length2):
                if (list1[p1] < list2[p2]):
                    merged.append(list1[p1])
                    p1 += 1
                else:
                    merged.append(list2[p2])
                    p2 += 1
            merged.extend(list1[p1:])
            merged.extend(list2[p2:])
            return merged
        return divide(nums)    
    
    
"""
This might well be the first time I implement a merge sort that looks
this elegant. I've implemented it a couple of times before, but it never
looked this fine.

It took me about 15 minutes to succesfully submit this. First attempt was
succesful.It beats 49% in terms of runtime and 14 % in terms of memory.

I should probably try to do it in place by passing pointers rather than lists,
and I should maybe try to do it iteratively once as well, but that's for another
time when i'm not dealing with recursion.
"""