# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:31:07 2021

@author: Nikita
"""

"""
Let's start with the basics:
    "anything" is an integer number in this case
    0^anything = 0 except for infinity
    1^anything = 1 except for infinity
    anything^0 = 0 except for 0 and infinity
    -1^anything = -1 or 1 depending on whether the number is odd or even
    -anything ^ anything is exactly the same as anything^anything*(-1)^anything
    [0,1) to a positive power converges to 0
    (1,0] to a negative power converges to 0
    everything else diverges
    
In hindsight, this was a very easy problem. The solution was binary 
exponentiation. Although I knew how to do it from cryptography, I had a few
hiccups whilst actually implementing it. 
"""




def function_pow(x : float, n : int) -> float:
    invert = False
    if n == 0:
        return 1
    elif n < 0:
        invert = True
    number = 1
    power = x
    n = abs(n)
    while (n != 0) :
        if n % 2 == 1 :
            number = number * power 
        power = power * power
        n //= 2
    if invert:
        return 1/number
    return number

def function_pow2(x,n): # won't work for function_pow2(0.00001, 2147483647))
    invert = False
    number = 1
    if (n < 0):
        invert = True    
    while (n != 0):
        number = x * number
        n += -1*n/abs(n)
    if invert:
        return 1.0/number
    return number
    
print(function_pow(-2,))
