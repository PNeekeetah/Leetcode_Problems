# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:51:21 2020

@author: Nikita
"""

import re
class Solution:
    
    def __init__(self) -> None:
        pass
    
    def bestSolution(self, s: str) -> int:
        s = s.strip()
        if (len(s) == 0):
            return 0
        start = 0
        sign = 1
        if (s[0] == "-"):
            start = 1
            sign = -1
        elif (s[0] == "-"):
            start = 1
            sign = 1
        result = "0"
        while ((start <= len(s)-1) and s[start].isdigit()):
            result += s[start]
            start += 1
            
        return min(max(sign * int(result),-2**31),2**31-1)
               
    def myAtoi(self, s: str) -> int:
        first_int = re.findall("^[\s]*[\+\-]?\d+", s)
        if (len(first_int) == 0):
            return 0
        first_int = int(first_int[0])
        return min(max(int(first_int),-2**31),2**31-1)
   
    


def main():
    test_case1 = "   + -321  + -+-++ +-    -+-2 3 5      412jkjk Hello world i - like -248 things and i have 2 horses"
    test_case2 = "    -42 321"
    test_case3 = "42"
    solution = Solution()
    assert( solution.myAtoi(test_case1) == 0)
    assert( solution.myAtoi(test_case2) == -42)
    assert( solution.myAtoi(test_case3) == 42)
    solution.bestSolution(test_case3)
    
    assert( solution.bestSolution(test_case1) == 0)
    assert( solution.bestSolution(test_case2) == -42)
    assert( solution.bestSolution(test_case3) == 42)
if __name__ == "__main__":
    main()

"""
###########
Seeing the success that RE had previously, i am going to build a regular 
expression that does the following :
    1. looks behind and checks whether characters is not numeric
    2. Look behind matches any number of + or -
    3. returns first instances of a number
    4. lookahead is not alphanumeric
############
    
Looking back on it, i think i did overcomplicate the problem quite a bit. 
All i had to do was find the first + or - followed by a number. If no such
thing existed, my ATOI shouldn't have returned anything to begin with. 

The regex i was able to come up with is : [\s]*[\+\-]?\d+ -> zero or more
whitespaces followed by 0 or 1 plus or minus and the number. I was trying 
to do smart things with lookbehinds and lookaheads and that basically set
me back by 24 hours. Anyhow, the current solution beats 83% of submissions.

The fastest solution does the following:
    1. Strips string of leading whitespaces.
    2. Checks if the first symbol is a -/ if it is, a sign is updated 
    accordingly and the start is set to the following symbol.
    3. Each element is checked whether it is a digit or not, and as 
    the index moves along, the digits are added to a "result" variable.
    4. The result variable is capped using the same min-max method and 
    returned. 

Takeaway:
    I spent way too much time beating around the bush, trying to find the 
    ideal regex without actually understanding what the problem required. 
    Although the best solution might be faster, i still prefer my own 
    because it looks more elegant.
    
    * After implementing it myself, i have serious doubts that it outperforms
    the regex implementation on average.

"""