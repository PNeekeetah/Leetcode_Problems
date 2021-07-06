# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 12:52:15 2021

@author: Nikita
"""

"""
Solution beats 11% in terms of runtime and
20% in terms of memory.

Took me 5 minutes to come up with this 
solution. 
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        numbers_dict = dict()
        array_size = len(arr)
        
        for num in arr:
            numbers_dict.setdefault(num, 0)
            numbers_dict[num] += 1
        
        occurences_list = [(occurences,number) for number,occurences in numbers_dict.items()]
        occurences_list.sort()
        print(occurences_list)
        
        min_set = 0
        total_occurences = 0
        index = len(occurences_list) - 1
        while total_occurences < array_size/2:
            total_occurences += occurences_list[index][0]
            index -= 1
            min_set += 1
        return min_set
        