# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 02:18:49 2021

@author: Nikita
"""

"""
Beats 35% in terms of runtime and 30% in terms
of memory usage.
"""

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        num_dict = dict()
        number_occurences_tuples = list()

        for number in nums:
            num_dict.setdefault(number,0)
            num_dict[number] += 1
        
        for number,occurences in num_dict.items():
            number_occurences_tuples.append((occurences,number))
        
        number_occurences_tuples.sort()
        
        most_frequent = [elem[1] for elem in number_occurences_tuples[-k:]]
        return most_frequent