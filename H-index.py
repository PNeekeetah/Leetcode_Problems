# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:05:25 2021

@author: Nikita
"""

"""
Took me 33 minutes

Runtime : beats 13% 
Memory : beats 95 %
"""

class Solution:
    def hIndex(self, citations: list) -> int:
        citations.sort()
        citations.reverse()
        h = 0
        for i, citations in enumerate(citations):
            if i + 1 <= citations:
                h = i + 1
        return h