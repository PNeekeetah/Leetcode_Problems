# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:27:08 2021

@author: Nikita
"""

"""
Beats 18% in terms of runtime and 26% in
terms of memory.

First time submission succeeded.

Took me less than 10 minutes to come up with this solution.
"""

def reverse_word(word : str) -> str:
    new_word = ""
    for i in range (len(word)-1,-1,-1):
        new_word += word[i]
    return new_word

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reversed_string = ""
        for i in range(len(words)-1):
            reversed_string = reversed_string + reverse_word(words[i]) + " "
        else:
            reversed_string += reverse_word(words[-1])
        return reversed_string