# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:15:08 2021

@author: Nikita
"""
"""
40:19 -> beats 5.22% in termms of runtime and 86% in terms of memory.
I got it in the fifth attempt in 40 minutes and 19.

"""

class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        """
        Highest frequency word first.
        Alphabetically second
        """
        # Create a frequency dictionary
        frequency = dict()
        for word in words:
            frequency.setdefault(word,0)
            frequency[word] += 1
        # Put words from the frequency dictionary into buckets
        frequency_dict = dict()
        for item in frequency.items():
            frequency_dict.setdefault(item[1],set())
            frequency_dict[item[1]].add(item[0])    
        frequency_tuples = []
        # Create tuples with the frequency first, followed by the set of words
        for item in frequency_dict.items():
            frequency_tuples.append((item[0],item[1]))
        # Sort tuples by frequency
        frequency_tuples.sort()
        frequency_tuples.reverse()
        solution = []
        for tup in frequency_tuples:
            # Create list out of each set and sort it; extend solution with it
            partial = list(tup[1])
            partial.sort()
            solution.extend(partial)
        return solution[0:k]
        
        
sol = Solution()
sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2)