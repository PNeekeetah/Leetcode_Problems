# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:00:47 2020

@author: Nikita
"""

array = [2,2,3,4,3,4,5,6,5,6,7]

"""
    Idea Zero :
        Just do an O(n^2) check and return when the element's
        pair isn't found
        
    First Idea:
        Use a hash map of the type {number : indices}
        Add all indices of the numbers in hashmap, return
        only the number which has a single appearance.
        
        -> Goes against O(1) space, but is O(n) time
    
    Second Idea : 
        Sort array, then check elements 2 by 2
        
        -> Goes against O(n) (O(n log(n)) at best) time, 
        but is O(1) space if sorting is done in place
        
    Third Idea : 
        Just XOR all elements, the only one without a pair
        will stand out. 
        
        -> Definitely both O(1) and O(n)
        
"""
acc = 0
for elem in array:
    acc ^= elem


# Best Runtime solution
acc = array[0]
for i in range(1,len(array)):
    acc ^= array[i]
    
    
"""
    My solution beat 43% of the other solutions. 
    
    Takeaway: 
        The best solution already put the first element
        in the accumulator. I didn't do that / otherwise,
        the solution is pretty much the same
        

"""