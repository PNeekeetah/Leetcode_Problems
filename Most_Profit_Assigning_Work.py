# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:35:23 2021

@author: Nikita
"""

class Solution:
    def maxProfitAssignment1(self, difficulty, profit, worker):
        diff_and_profit = []
        for diff,prof in zip(difficulty, profit):
            diff_and_profit.append((diff,prof))
        diff_and_profit.sort()
        worker.sort()
        
        total_profit = 0
        max_so_far =0
        iterator = 0
        
        for w in worker:
            while (iterator < len(difficulty) and 
                   w >= diff_and_profit[iterator][0]):
                max_so_far = max(diff_and_profit[iterator][1],max_so_far)
                iterator += 1
            total_profit += max_so_far 
        return 
    
    
"""
I gave up after 24 minutes/ I realised it is a greedy problem, and as such
i knew there's likely no way for me to solve it without spending a couple
of hours on it. 

The only solution I could come up with was the O(n^2) one.

My friend did something more clever: he mapped the difficulties and profits
together as a list of tuples, then he sorted by difficulty. He then sorted
the workers.

if worker_1 can complete the first 3 jobs, due to the sorting, worker_2 can 
complete the first 3 jobs as well; as such, there's no need to start from 
the beginning of the list every time. Also, we keep track of the maximum 
profit so far by job n.

The runtime would be n log n, which is a reduction from my O(n^2).

Kudos to him for his solution; this code is the result of talking about the
problem with him.

Since I gave up, I will not record any time or memory for this problem.
"""
    
