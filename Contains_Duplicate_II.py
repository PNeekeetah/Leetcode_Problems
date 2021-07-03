# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:57:30 2021

@author: Nikita
"""

"""
Took me 6 minutes to come up with this but it's worst 
than all solutions in terms of memory and runtime. Huh?

I checked the second part and it's definitely linear.
Is setdefault() that bad?

Well, first time submission succesful nonetheless.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        indexes_dict = dict()
        duplicate_set = set()
        
        for index,number in enumerate(nums):
            indexes_dict.setdefault(number,[]).append(index)
            if len(indexes_dict.get(number)) > 1:
                duplicate_set.add(number)
        
        for number in duplicate_set:
            index_list = indexes_dict[number]
            for index1,index2 in zip(index_list[0:-1],index_list[1:]):
                if abs(index1-index2) <= k:
                    return True
                
        return False
        