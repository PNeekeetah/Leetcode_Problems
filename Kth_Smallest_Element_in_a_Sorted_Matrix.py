# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:45:53 2021

@author: Nikita
"""

"""
Beats 59% in terms of runtime and 10% in terms of memory usage.

Sadly, first time I submitted was not succesful because I 
misinterpreted what was required.

Took me ... probably around 1 hour to do this.
"""

class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        numbers_dict = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                key = matrix[i][j]
                numbers_dict.setdefault(key,0)
                numbers_dict[key] += 1
                
        sorted_keys = list(numbers_dict.keys())
        sorted_keys.sort()
        
        index = -1
        while k > 0:
            index += 1
            key = sorted_keys[index]
            current = numbers_dict[key]
            k -= current
        
        return sorted_keys[index]