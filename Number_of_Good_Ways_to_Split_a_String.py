# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:05:24 2021

@author: Nikita
"""

class Solution:
    def numSplits(self, s: str) -> int:
        head_tail = {}
        tail_head = {}
        diff_h_t = 0
        diff_t_h = 0
        h_t_sum = []
        t_h_sum = []
        for i in range(len(s)):
            if head_tail.get(s[i]) == None:
                diff_h_t += 1
                h_t_sum.append(diff_h_t)
                head_tail[s[i]] = 1
            else:
                h_t_sum.append(diff_h_t)
                
        for i in range(len(s)-1,-1,-1):
            if tail_head.get(s[i]) == None:
                diff_t_h += 1
                t_h_sum.insert(0,diff_t_h)
                tail_head[s[i]] = 1
            else:
                t_h_sum.insert(0,diff_t_h)
        
        eq = 0
        for i in range(len(t_h_sum)-1):
            if h_t_sum[i] == t_h_sum[i+1]:
                eq += 1
        
        return eq
    
    def numSplits1(self, s: str) -> int:
        head_tail = set()
        tail_head = set()
        t_h_sum = []

        for i in range(len(s)-1,-1,-1):
            tail_head.add(s[i])
            t_h_sum.insert(0,len(tail_head))
            
        eq = 0
        for i in range(len(s)-1):
            head_tail.add(s[i])            
            eq += (len(head_tail) == t_h_sum[i+1])

        return eq
    
    def numSplits2(self, s: str) -> int:
        head_tail = set()
        tail_head = set()
        t_h_sum = []

        for i in range(len(s)-1,-1,-1):
            tail_head.add(s[i])
            t_h_sum.append(len(tail_head))
            
        eq = 0
        for i in range(len(s)-1):
            head_tail.add(s[i])            
            eq += (len(head_tail) == t_h_sum[len(t_h_sum)-i-2])

        return eq

"""
Problem finished in 22:39 seconds. First time successful.

Beats 5 in terms of runtime and 8 percent in terms of memory.

Working on optimising in right now.

numSplits1 is a shorter (and slightly more optimized) 
version. Beats 5% in terms of runtime and 20% in terms of memory.

I discovered why it was slow -> insert is shifts all terms by 1! 
Ammended that and now I've got a runtime that beats 92%.

"""