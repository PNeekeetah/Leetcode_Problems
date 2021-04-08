# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:29:10 2021

@author: Nikita
"""
import math as m

class Solution:
    def kClosest(self, points: list(), k: int) -> list(): # my solution
        mag_array = []
        for point in points:
            mag_array.append((point[0]**2 + point[1]**2,point))
        mag_array.sort()
        answer = []
        for i in range(k):
            answer.append(mag_array[i][1])
        return answer
    
    def kClosest1(self, points: list(), k: int) -> list(): # his solution
        points.sort(key=lambda x: m.sqrt(x[0]**2+x[1]**2))
        return points[:k]
    
"""
First time succesful, 11:32. Beats 67% in terms of runtime and 44% in terms of memory.

"""