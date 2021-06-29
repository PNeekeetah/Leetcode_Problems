# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:46:37 2021

@author: Nikita
"""

"""
Took me about 5 minutes to come up with this solution.
It beats 65% in terms of runtime and 98% in terms of
memory.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_dict = dict()
        for index,number in enumerate(numbers):
            number_dict[target-number] = index
        
        for index,number in enumerate(numbers):
            if number in number_dict and index != number_dict.get(number):
                return [index+1,number_dict.get(number)+1]
