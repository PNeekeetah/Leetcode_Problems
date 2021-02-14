# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:34:45 2021

@author: Nikita
"""

import re

strs = "Strings"
string1 = "strings"
string2 = "strings are life"
strings = ["string", "stri", "stringent", "struck","stroke", "strike", "straciatella"]
strings2 =["racecar", "race", "rachel", "random"]
strings3 = [""]
strings4 = ["anime"]
strings5 = ["analysis", "analretentive"] 
strings6 = ["dog", "cat", "grandpa"]
strings7 = ["cir", "car"]

# Best solution idea
long = string1
while (string2.find(long) !=  0) : 
    long = string1[0 : len(long)-1]
    
print(long)
    

class Solution(object):
    def __init__(self):
        return None
    
    def longestCommonPrefix(self, strs : list):
        if (len(strs) == 0 ):
            return ""
        elif(len(strs) == 1):
            return strs[0]
        else:
            comp1 = strs.pop(0).encode("ASCII")
            longest_prefix = len(comp1)
            
            for string in strs:
                current_prefix = 0
                comp2 = string.encode("ASCII")
                for byte1,byte2 in zip(comp1, comp2):
                    if (not byte1 ^ byte2):
                        current_prefix += 1
                    else:
                        break
                if (current_prefix < longest_prefix):
                    longest_prefix = current_prefix
                if(not longest_prefix):
                    return ""
                
        return strs[0][0:longest_prefix]


    def bestRuntimeSolution(self, strs: list):
        if len(strs)==0:return ""
        long=strs[0]
        strs=strs[1:]
        for i in strs:
            while i.find(long)!=0:
                long=long[0:len(long)-1]
            
        return(long)


sol = Solution()
print(sol.longestCommonPrefix(strings7))                

"""
The very first solution I wanted to build for this problem involved iterating
through all strings and comparing them against each other. 

I am doing almost the exact same thing with the bytes here, but rather than 
comparing the characters with ==, I am checking whether the XOR of their bytes
is 0. 

I made a mistake in the sense that I used a "continue" rather than a "break"
statement. 

I also know that using breaks and continues isn't precisely "clean" code.

Nonetheless, it took me 52 minutes and 23 seconds to come up with this. My 
solution breats 32 % of Python 3 submissions in terms of runtime and it beats
95% in terms of memory usage. 

Now I will compare this with the best solution.

The best runtime solution, much in the same way I did, used 2 loops to iterate 
through the strings. Truthfully, no byte conversion is actually needed, This
could be the reason why mine was so slow.
"""