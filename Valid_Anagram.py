# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:43:09 2020

@author: Nikita
"""

class Solution:
    
    def __init__(self) -> None:
        pass
    
    def bestSolution(self, s: str, t: str) -> bool:
        pass
    
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Parameters
        ----------
        s : str
            String 1.
        t : str
            String 2.

        Returns
        -------
        bool
            True if string 1 is an anagram of string 2.
        """
        s_set = set(s)
        t_set = set(t)
        
        if (t_set != s_set):
            return False
        
        for char in s_set:
            if(s.count(char) != t.count(char)):
                return False
            
        return True
    
    
def main ():
    solution = Solution()
    is_anagram1 = solution.isAnagram("anagram","nagaram")
    is_anagram2 = solution.isAnagram("kitty", "dog")
    is_anagram3 = solution.isAnagram("äëüëö", "äöëëü")
    is_anagram4 = solution.isAnagram("äëüëö", "äöëeeeëü")

if __name__ == "__main__":
    main()
        
"""
My solution converted both strings to sets, compared the sets and 
returned False if the sets were different. Otherwise, it continued.
Then, it counted the occurence of each element/ if the occurences
were different once, the program returns False.

My solution beat 98.81% of solutions in terms of runtime.

Takeaway:
    The best solution checked if the lengths were equal, and then for each
    character in lowercase ascii it checked whether their counts were equal.
"""
        