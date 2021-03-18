# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:26:54 2021

@author: Nikita
"""

import random as r
import matplotlib.pyplot as plt

calls = 0

class Solution():
    def rand7(self):
        global calls
        calls += 1
        return r.randint(1,7)
    
    def rand10(self):           # average 2.43 calls
        row = self.rand7()-1
        col = self.rand7()
        num = col + row*7
        while (num > 40):
            row = self.rand7()-1
            col = self.rand7()
            num = col + row*7
        
        return 1 + (num-1)%10
    
    def rand10_1(self):         # average 2.17 calls
        row = self.rand7()-1
        col = self.rand7()
        num = row*7 + col
        lim = 40
        m_lim = 49
        while (num > lim):
            num = (num - lim - 1)*7 + self.rand7()
            m_lim = (m_lim - lim-1)*7 + 7
            lim = m_lim - m_lim%10
                    
        return 1 + (num-1)%10
    
solution = Solution()
TIMES = 10000
x = [solution.rand10_1() for i in range (TIMES)]
plt.hist(x)
print(calls/TIMES)            