# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 01:59:38 2020

@author: Nikita
"""
import re

class Solution:
    
    def __init__(self) -> None:
        pass
    
    def bestSolution(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
    
    def strStrRe(self, haystack: str, needle: str) -> int:
        """
        Parameters
        ----------
        haystack : str
            The string where "needle" must be found.
        needle : str
            The string which must be found within "haystack".

        Returns
        -------
        int
            Index of the first occurence, -1 if not found or 0 if needle is 
            the empty string. 
        """
        if (len(needle) == 0):
            return 0
        firstOccurence = re.search(needle, haystack)
        if (firstOccurence):
            return firstOccurence.span()[0]
        else:
            return -1
        
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Parameters
        ----------
        haystack : str
            The string where "needle" must be found.
        needle : str
            The string which must be found within "haystack".

        Returns
        -------
        int
            Index of the first occurence, -1 if not found or 0 if needle is 
            the empty string. 
        """
        if (len(needle) == 0):
            return 0
        end = len(needle) - 1
        for i in range(len(haystack) - end):
            if (haystack[i:i+end+1] == needle):
                return i 
        return -1
    
def main():
    solution = Solution()
    haystack1 = "the quick brown fox jumps over the lazy dog"
    needle1 = "brown fox"
    needle2 = "dogf"
    needle3 = "the"
    needle4 = ""
    try1 = solution.bestSolution(haystack1, needle1)
    try2 = solution.strStrRe(haystack1, needle2)
    try3 = solution.strStrRe(haystack1, needle3)
    try4 = solution.bestSolution(haystack1, needle4)
    try5 = solution.strStr("mississippi","issipp")
    
if __name__ == "__main__":
    main()
                
hello = set("321")
penis = set("123")
pula = set("213")
peeeniss = set("32131211212313213231213212321232321231231222221131232132")
"""
It feels like using regex for this problem is a bit like cheating. I will 
write 2 versions, one that uses regex and one that doesn't.

Everything between ## ## is wrong. 
#########################################
For the version that doesn't use regex:
    1. Check if the length of needle is 0 and return 0 if so
    2. Start iterating through each character of the string/
       Whenever the first character matches the first character
       of needle, save the index and continue iterating. If the entire
       string is found, return the index, otherwise continue.
       
I am not sure whether i should use nested ifs for the loop or 
a more complicated formula.

First option:
start = 0
end = len(needle)
for i in range(len(haystack)):
    if (needle[start] == haystack[i] ):
        start += 1
        if (start == end):
            return i - end + 1
    else:
        start = 0

Second option:
start = 0
end = len(needle)
for i in range(len(haystack)):
    start = (start*(haystack[i] == needle[start]) 
              + (haystack[i] == needle[start]))
    if (start == end):
        return i - end + 1
    
I do feel like the second option is more clever.
##########################################
As for the one done using regex, it's just a matter of using search and span.

The regex one beats 14% of submissions. The other one is wrong, for i've 
failed to consider what'd happen for a string such as this : find abc in ababc

The ammended version now beats 96.58 % of submissions. At each step, simply
check whether a slice of equal length as needle is equal to needle. Example 
run :

issipp = needle
mississippi = haystack
missis != issipp
ississ != issipp
ssissi != issipp
sissip != issipp
issipp == issipp return I.

The best solution does : 
    if needle in haystack:
        return haystack.index(needle)
    
That is a lot smarter than what i've done.
"""