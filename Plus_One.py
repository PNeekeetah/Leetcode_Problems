# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:08:14 2020

@author: Nikita

    A number of n digits is expressed as
    an array with n integer.
    
    Add 1 to the array.
    
    Simplest case is a number of the form xxxx1-8
    But what do you do when it cascades?
"""


# Test cases
digits1 = [1,0,0,0,0,1]
digits2 = [1,2,3,4,5,6,7]
digits3 = [9,9,9,9,9]
digits4 = [9,1,9,9,9,9]
digits5 = [0]
digits6 = [2,0,2]

class Solution():
    
    def __init__(self):
        None
        
    def generatorSolution (self, digits: list) -> list:
        number = 0
       
        for elem in digits:
            number = number*10 + elem
        
        number += 1
        return [int(i) for i in str(number)]

    def plusOne (self, digits: list) -> list:
        carry = 0
        digits[-1] += 1
        
        for i in range(len(digits)-1,-1,-1):
            digits[i] +=  carry 
            carry = (digits[i] > 9)
            digits[i] %= 10
        
        if (carry):
            digits.insert(0,1)
        
        return digits
    
    def bestRuntime (self, digits : list) -> list:
        carry = 0
        digits[-1] += 1
        
        for i in range(len(digits)-1,-1,-1):
            digits[i] +=  carry 
            carry = (digits[i] > 9)
            digits[i] %= 10
            # If carry is 0, no more sense to continue.
            if(not carry):
                return digits
        
        if (carry):
            digits.insert(0,1)
        
        return digits

solution = Solution()

# Assertions should succeed after code modifications
assert (solution.generatorSolution(digits1) == [1, 0, 0, 0, 0, 2])
assert (solution.generatorSolution(digits2) == [1, 2, 3, 4, 5, 6, 8])
assert (solution.generatorSolution(digits3) == [1, 0, 0, 0, 0, 0])
assert (solution.generatorSolution(digits4) == [9, 2, 0, 0, 0, 0])
assert (solution.generatorSolution(digits5) == [1])
assert (solution.generatorSolution(digits6) == [2,0,3])


"""
    This beats 37 % of submissions with a runtime of 24 ms
        ######################################
        carry = 0
        digits[-1] += 1
        
        for i in range(len(digits)-1,-1,-1):
            digits[i] = digits[i] + carry 
            carry = (digits[i] == 10)
            digits[i] -= 10*carry
        
        if (carry):
            digits.insert(0,1)
        
        return digits
        ######################################
        Idea is:
            increment rightmost integer by 1
            a carry bit is set to 1 if the integer goes out of range 0-9
            subtract from the digit 10 if out of range
            
            Finally, append a 1 at the end 
            
        Takeaway:
            The very best solution in terms of runtime simply
            called the return statement if carry is 0.
            
            Another solution ran 1 for loop to convert the number
            to an int,added 1, then ran a generator that converted 
            the number from a string to a list of ints
            
        
    
"""
