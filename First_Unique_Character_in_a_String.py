# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:38:19 2020

@author: Nikita
"""

class Solution:
    
    def __init__(self) -> None:
        pass
    
    def best_solution(self, s : str) -> int:
        reference = "abcdefghijklmnopqrstuvwxyz"
        unique_chars = []
        for char in reference:
            first_occ = s.find(char)
            if (first_occ >= 0 ):
                second_occ = s.find(char, first_occ + 1)
                if (second_occ < 0):
                    unique_chars.append(first_occ)
                else:
                    continue
        if (len(unique_chars) == 0):
            return -1
        else:
            return min(unique_chars)
                
    
    # My solution
    def firstUniqChar(self, s : str) -> int:
        char_dict = dict()
        for char in s:
            if (char_dict.get(char)):
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        for i in range(len(s)):
            if(char_dict[s[i]] == 1):
                return i
        
        return -1
        
        
def main():
    test_cases = ["hello","anagram","armageddon","president","supercalifragilisticexpialidocious",
                  "thequickbrownfoxjumpsoverthelazydog","captaincrunchcereals",
                  "cccccca","newpythonprogramsmakemeenthusiastic",
                  "thenoveltyofthisapproachwillrevolutionizetheworld",
                  "gedankexperiment"] 
    solution = Solution()
    results = [0, 1, 1, 0, 9, 3, 2, 6, 2, 9, 0]
    solution_results = []
    for test in test_cases: 
        solution_results.append(solution.firstUniqChar(test))
    
    assert(results == solution_results)
    
if __name__ == "__main__":
    main()
            
"""
In my solution, i build a hash map to count the occurences and then i return
the very first occurence equal to 1. My solution beat 67 percent if submisions
in terms of time.

    Takeaway:
        The best solution used the string "abcdefghijklmnopqrstuvwxyz" as a 
        reference and for each element in the reference string, it appended the
        index of an element if it appeared only once. 
        At the end, the smallest index is returned. 
"""