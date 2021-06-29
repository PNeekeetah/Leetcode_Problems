# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 22:17:09 2021

@author: Nikita
"""

"""
Took me less than 10 minutes to code this.
It beats 42% in terms of runtime and 0%
in terms of memory.

4th time submission sucessful. The fact 
that I could have multiple white spaces 
tripped me. 
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split(" ")
        valid_words = [word for word in words_list if word != ""]
        reversed_words = ""
        for i in range (len(valid_words)-1,0,-1):
            reversed_words += valid_words[i] + " "
        else:
            reversed_words += valid_words[0]
        return reversed_words
            