# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 23:17:08 2021

@author: Nikita
"""

"""
Beats 7% in terms of runtime and 53%
in terms of memory usage.

First time submission succesful.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = dict()
        longest_non_repeating = 0
        window_start = 0
        window_end = 0
        while window_end < len(s):
            char = s[window_end]
            char_dict.setdefault(char,0)
            char_dict[char] += 1
            if char_dict[char] == 1:
                window_end += 1
            else:
                longest_non_repeating = max(window_end - window_start ,longest_non_repeating)
                window_start = window_start + 1
                window_end = window_start
                char_dict.clear()
        else:
            longest_non_repeating = max(window_end - window_start, longest_non_repeating)
        
        return longest_non_repeating
            