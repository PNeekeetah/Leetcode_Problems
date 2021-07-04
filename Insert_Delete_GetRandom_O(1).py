# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 03:22:58 2021

@author: Nikita
"""

"""
First time submission succesful.

Beats 8% in terms of runtime and 0% in
terms of memory.

I will go right ahead and admit that 
I had no idea how I might design this from
scratch without using python's set and 
the random library.

I had a look at the solutions for
this problem and saw that absolutely
everybody else used python's set so I
went ahead and ditched the shame and
implemented this in less than 3 minutes.

First time submission succesful, but I 
still wish i'd be able to design it from
scratch.
"""

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.set:
            self.set.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.set))
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()