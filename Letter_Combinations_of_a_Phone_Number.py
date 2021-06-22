# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 22:34:29 2021

@author: Nikita
"""

"""
Beats 61.61% in terms of runtime and it beats 29.37 in terms of memory
I think it took me about 30-45 minutes to come up with this solution

I applied some hardware principles in this problem i.e. the modularisation
I think I could have come up with a formula to deduce which character should
appear, however, I thought that designing an object that took care of that 
for me automatically would be better.

I'm particularly proud of this solution.
"""

class CounterModule:
    def __init__ (
            self,
            count : int = 3, 
            feed_out : "CounterModule" = None,
    ) -> None:
        """
        count - up until you end up counting
        feed_out - a module into which this feeds
        number - from 0-2 OR 0-3 depending on count_to_3
        """
        self.count = count
        self.feed_out = feed_out
        self.number = 0
        
    def increase(self) -> None:
        self.number += 1
        self.number %= self.count
        if self.number == 0 and self.feed_out is not None:
            self.feed_out.increase()
        
            
    def get(self) -> int:
        return self.number
            

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_keys = [
            [],
            [],
            ["a","b","c"],
            ["d","e","f"],
            ["g","h","i"],
            ["j","k","l"],
            ["m","n","o"],
            ["p","q","r","s"],
            ["t","u","v"],
            ["w","x","y","z"],
        ]
        
        three_letters = {
              2,3,
            4,5,6,
              8,
        }
        
        four_letters = {
            7,  9,
        }
        
        counter_max = []
        
        for c in digits:
            if int(c) in three_letters:
                counter_max.append(3)
            else:
                counter_max.append(4)
        
        counter_init = []
        
        for i in range(len(counter_max)):
            if i == 0:
                counter_init.append(
                    CounterModule(counter_max[i])
                )
            else:
                counter_init.append(
                    CounterModule(
                        counter_max[i],
                        counter_init[i-1]
                    )
                )
            
        
        if len(counter_max) > 0:
            max_count = 1
        else:
            max_count = 0
        
        for number in counter_max:
            max_count *= number
        
        all_strings = []
        for i in range(max_count):
            string = ""
            for i,cnt in enumerate(counter_init):
                string += phone_keys[int(digits[i])][cnt.get()]
            all_strings.append(string)
            counter_init[-1].increase()
        
        return all_strings
            