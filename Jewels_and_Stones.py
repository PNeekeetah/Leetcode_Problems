# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:53:56 2021

@author: Nikita
"""

"""
Took me about 3 minutes to write this.

Beats 63% in terms of runtime and none
in terms of memory usage.

First submission succesful.
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = {jewel for jewel in jewels}
        total_jewels = 0
        for stone in stones:
            if stone in jewels_set:
                total_jewels += 1
        return total_jewels
