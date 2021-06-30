# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:02:04 2021

@author: Nikita
"""

"""
Took me about 5 minutes to implement this solution
It beats 81% in terms of runtime and 88 % in terms
of memory.

First time submission succesful.

I included one of my earlier attempts as well for
reference.
"""

import numpy as np

class Solution:
    
    def containsDuplicate(self, nums: list) -> bool: # second attempt
        duplicates_set = set()
        
        for number in nums:
            if number not in duplicates_set:
                duplicates_set.add(number)
            else:
                return True
        
        return False
    
        
    def containsDuplicate1(self, nums):         # first attempt
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupes = np.zeros(len(nums),dtype = int)
        for elem in nums:
            dupes[elem] = dupes[elem] + 1
        
        for elem in dupes:
            if (elem > 1):
                return True
        return False
        