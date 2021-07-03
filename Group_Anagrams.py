# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 01:24:27 2021

@author: Nikita
"""

"""
Beats 11% in terms of runtime and 36% in terms
of memory.

First time submission succesful.
"""        

def get_key(string : str) -> str:
    reference = "abcdefghijklmnopqrstuvwxyz"
    char_dict = dict()
    for char in string:
        char_dict.setdefault(char,0) 
        char_dict[char] += 1 
    
    return "".join(letter+str(char_dict.get(letter)) for letter in reference if char_dict.get(letter) is not None)
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        solution = list()
        keys = set()
        
        for string in strs:
            key = get_key(string)
            anagram_dict.setdefault(key,[]).append(string)
            keys.add(key)
        
        for key in keys:
            solution.append(anagram_dict[key])
        
        return solution