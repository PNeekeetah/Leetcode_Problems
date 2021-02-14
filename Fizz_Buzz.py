# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 02:10:25 2020

@author: Nikita
"""

n1 = 15

class Solution():
    
    def __init__(self):
        None
        
    def fizzBuzz (self, n: int) -> list:
        fblist = []
        for elem in range(1,n+1):
            if (elem%3 == 0 and elem%5 == 0):
                fblist.append("FizzBuzz")
            elif (elem%3 == 0):   
                fblist.append("Fizz")
            elif (elem%5 == 0):
                fblist.append("Buzz")
            else:
                fblist.append(str(elem))
        return fblist

solution = Solution()
print(solution.fizzBuzz(n1))


"""
    I decided to implement it via a for loop.
    If the element is divisible by both 5 and 3, append FizzBuzz
    If the element is divisible by 3, append only Fizz
    If the element is divisible by 5, append only Buzz
    Append the string of the element otherwise.
    
    My solution sits around the mean in terms of time complexity,
    at 28 ms. It's linear alright.
    
    Takeaway:
        All solutions for all time brackets LOOK LITERALLY the same.
        My fizz buzz is as good as it can be. 

"""