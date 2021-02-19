# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:32:22 2021

@author: Nikita
"""
import random

total_products = 100
bad_version = random.randint(1,total_products)

def isBadVersion(version : int) -> bool:
    global bad_version 
    return (version >= bad_version)
    
class Solution:
    """
    Second version with 1 less IsBadVersion call
    """
    def firstBadVersion(self, n : int) -> int:
        interval_min = 0
        interval_max = n
        halfway = (interval_max+interval_min)//2
        while (interval_max - interval_min > 1):
            if(isBadVersion(halfway)):
                interval_max = halfway
            else:
                interval_min = halfway
            halfway = (interval_max+interval_min)//2
        return interval_max
    
    """
    Initial version that checked at the end -> had to make sure that the
    case with 1 and 2 products was covered.
    """
    def firstBadVersion(self, n : int) -> int:
        interval_min = 1
        interval_max = n
        halfway = (interval_max+interval_min)//2
        while (interval_min != halfway):
            if(isBadVersion(halfway)):
                interval_max = halfway
            else:
                interval_min = halfway
            halfway = (interval_max+interval_min)//2
        if (isBadVersion(halfway)):
            return halfway
        else:
            return interval_max

    

        

    
solution = Solution()
print(solution.firstBadVersion(total_products))
            

"""

This can be done lineary, but it can be done in log2(n) which is better

Finished this after 48 minutes and 43 seconds.

3rd submission was succesful. Beats 80% in terms of
runtime, but for some reason it's really bad in terms
of memory.

Although I guessed you could do it via a binary search, the test case 
with 1 and 2 products tripped me up. Oops.

With this problem solved, I FINALLY GET TO DO SOME DYNAMIC PROGRAMMING
PROBLEMS !!!


"""