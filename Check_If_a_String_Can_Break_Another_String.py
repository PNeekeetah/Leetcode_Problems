# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:55:46 2021

@author: Nikita
"""

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        char_list1 = [c for c in s1]
        char_list2 = [c for c in s2]
        char_list1.sort()
        char_list2.sort()
        one_breaks_two = True
        two_breaks_one = True
        for i in  range(len(char_list1)):
            one_breaks_two = one_breaks_two and (char_list1[i] >= char_list2[i])
            two_breaks_one = two_breaks_one and (char_list2[i] >= char_list1[i])
        return one_breaks_two or two_breaks_one
        