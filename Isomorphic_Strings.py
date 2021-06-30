# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:44:39 2021

@author: Nikita
"""

"""
Took me about 15 minutes to solve this.
It beats 72 % in terms of runtime and 
48% in terms of memory usage.

Third attempt succesful.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # 22:32
        char_dict = dict()
        mappings = set()
        for char1,char2 in zip(s,t):
            if char1 not in char_dict:
                char_dict[char1] = char2
                if char2 not in mappings:
                    mappings.add(char2)
                else:
                    return False
            else:
                if char_dict.get(char1) != char2:
                    return False
        return True
            