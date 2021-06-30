# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 22:08:26 2021

@author: Nikita
"""

"""
Took me 3 minutes to come up with this solution, and 
that's because I was unsure whether "intersection"
was a function or not.

Well, it's a set so it had to be.

Beats 55.24 in terms of runtime and 0% in terms of memory

Weirdly, if I one-line it, I get better than 93% runtime 
and better than 72% memory usage. Hmmmm

"""

class Solution:
    def intersection(self, nums1: list, nums2: list) -> set:
        nums1_set = {num for num in nums1}
        nums2_set = {num for num in nums2}
        return nums1_set.intersection(nums2_set)
    
    def intersection_oneline(self, nums1: list, nums2: list) -> set:
        return {num for num in nums1}.intersection({num for num in nums2})