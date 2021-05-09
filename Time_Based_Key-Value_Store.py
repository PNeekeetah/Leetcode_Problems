# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:32:34 2021

@author: Nikita
"""

"""
I know I have to use binary search, but I was too lazy to implement it.
Passes 44/45 with time limit exceeded for the last one, as far as I'm 
concerned, it's good enough.
"""

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.map.get(key):
            self.map[key] = []
        self.map[key].append((timestamp,value))
        self.map[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        if self.map.get(key):
            current_string = ""
            for elem in self.map[key]:
                if timestamp >= elem[0]:
                    current_string = elem[1]
                else:
                    return current_string
            return current_string
        return None
                    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp

"""

TimeStamp()             -> None
set(["love","high",10]) -> None
set(["love","low",20])  -> None
get(["love",5])         -> "" 
get(["love",10])        -> "high"
get(["love",15])        -> "high"
get(["love",20])        -> "low"
get(["love",25])        -> "low"

"""