# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:35:26 2021

@author: Nikita
"""

class Solution:
    def printVertically(self, s: str) -> list(str):
        words = list(s.split(" "))
        index = 0
        maxlen = 0
        for w in words:
            if (len(w) > maxlen):
                maxlen = len(w)
        vert = []
        for i in range(maxlen):
            vert.append("")

        for index in range(maxlen):
            for w in words:
                if (index < len(w)):
                    vert[index] = vert[index] + w[index]
                else:
                    vert[index] = vert[index] + " "
        for i in range(len(vert)):
            vert[i] = vert[i].rstrip()
        return vert
    
"""
Solved in 23 minutes and 51 seconds. First submission succesful.
Beats 92.59 % in terms of runtime and 55.84 in terms of memory.
"""