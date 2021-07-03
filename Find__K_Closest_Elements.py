# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:19:10 2021

@author: Nikita
"""


"""
Beats 33% in terms of runtime and 69 % in terms of memory
"""

def first_is_closer(number1 : int, number2 : int, target : int) -> bool:
    smaller_distance = abs(number1 - target) < abs(number2 - target)
    equal_distance = abs(number1 - target) == abs(number2 - target)
    smaller_number = number1 < number2
    return smaller_distance or equal_distance and smaller_number

class Solution:
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        """
        |a-x|  < |b-x| OR
        |a-x| == |b-x| and a < b
        """
        # can optimize it with these if statements
        if arr[-1] < x :
            return arr[-k:]
        elif arr[0] > x:
            return arr[0:k]
        else:
            window_start = 0
            window_end = len(arr)-1
            while window_end - window_start > k - 1:
                number1 = arr[window_start]
                number2 = arr[window_end]
                if first_is_closer(number1, number2, x):
                    window_end -= 1
                else:
                    window_start += 1
            return arr[window_start:window_end+1]
                
            
        