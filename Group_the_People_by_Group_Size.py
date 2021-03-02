# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:50:05 2021

@author: Nikita
"""

class Solution:
    def groupThePeople(self, groupSizes: list) -> list(list()):
        person_dict = {}
        for i in range(len(groupSizes)):
            person_dict[i] = groupSizes[i]
        group_sizes = set(person_dict.values())
        all_groups = {}
        while len(groupSizes) > 0:
            person = len(groupSizes) - 1
            element = groupSizes.pop()
            if not(all_groups.get(element)):
                all_groups[element] = [person]
            else:
                all_groups[element].append(person)
        sol = []
        for key in all_groups.keys():
            current = all_groups[key]
            for i in range(0, len(current),key):
                print(i)
                sol.append(current[i:(i+key)])
        
        return sol
                
        return None
    
    def groupThePeople2(self, groupSizes: list) -> list(list()):
        all_groups = {}
        while len(groupSizes) > 0:
            person = len(groupSizes) - 1
            element = groupSizes.pop()
            if not(all_groups.get(element)):
                all_groups[element] = [person]
            else:
                all_groups[element].append(person)
        sol = []
        for key in all_groups.keys():
            current = all_groups[key]
            for i in range(0, len(current),key):
                sol.append(current[i:(i+key)])
        
        return sol
        
    
"""
Written as part of my daily submissions with my friend.

Solution took 23 minutes and 38 seconds to write.

It beats 89% in terms of runtime and 15% in terms of
memory.

Likely, there is some uneeded step.

I noticed that there were some unneeded parts in my solution. This one (2nd)
beats 96% in terms of speed and 76% in terms of memory.
"""