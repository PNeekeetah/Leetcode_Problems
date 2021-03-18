# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:09:24 2021

@author: Nikita
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 30 degrees per hour + 30/60 degrees per minute
        # 5 degrees per minute
        h = (hour*30)%360 + minutes/2
        m = (minutes*6)%360
        return min(abs(h-m),360 - abs(h-m))
        
"""
Took me 31 mintues to solve this (I didn't manage to get a succesful submission
                                  the first time).
Beats 59% in terms of runtime and 45% in terms of memory, tho
i don't know how.

"""            